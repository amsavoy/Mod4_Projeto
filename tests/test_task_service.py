"""
Suite de testes para geração de 50 senhas complexas com tamanhos variáveis.
Objetivo: Validar qualidade, segurança e diversidade das senhas geradas.
"""

import pytest
import sys
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'app'))

from main import PasswordGenerator, PasswordSuggester, PasswordValidator


class TestComplexPasswordGeneration:
    """Suite completa de testes para geração de 50 senhas com tamanhos variáveis."""

    @pytest.fixture
    def password_generator(self):
        """Fixture: Cria um gerador de senhas com todas as categorias habilitadas."""
        return PasswordGenerator(
            include_upper=True,
            include_lower=True,
            include_digits=True,
            include_punctuation=True
        )

    @pytest.fixture
    def password_suggester(self, password_generator):
        """Fixture: Cria um sugestor de senhas baseado no gerador."""
        return PasswordSuggester(password_generator)

    @pytest.fixture
    def varied_password_sizes(self):
        """Fixture: Retorna 50 tamanhos variáveis de senhas (8 a 30 caracteres)."""
        # Distribuição: gera exatamente 50 tamanhos
        sizes = []
        for size in range(8, 31):  # 8 a 30 caracteres (23 tamanhos)
            sizes.extend([size] * 2)  # 2 senhas por tamanho = 46 senhas
        # Adicionar 4 senhas extras com tamanhos variados
        sizes.extend([10, 15, 20, 25])
        return sizes

    def test_generate_50_complex_passwords_varied_sizes(self, password_generator, varied_password_sizes):
        """
        Testa se 50 senhas complexas podem ser geradas com tamanhos variáveis.
        Valida que cada senha atende aos critérios de complexidade.
        """
        generated_passwords = []

        for password_size in varied_password_sizes:
            PasswordValidator.validate_length(password_size)
            password = password_generator.generate(password_size)
            generated_passwords.append(password)

        # Validações gerais
        assert len(generated_passwords) == 50, "Deve gerar exatamente 50 senhas"
        assert all(isinstance(p, str) for p in generated_passwords), "Todas devem ser strings"
        assert all(len(p) > 0 for p in generated_passwords), "Nenhuma senha pode estar vazia"

    def test_all_50_passwords_have_correct_length(self, password_generator, varied_password_sizes):
        """Valida que cada uma das 50 senhas tem o comprimento solicitado."""
        for expected_size in varied_password_sizes:
            password = password_generator.generate(expected_size)
            assert len(password) == expected_size, \
                f"Senha deveria ter {expected_size} chars, mas tem {len(password)}"

    def test_all_50_passwords_contain_required_character_types(self, password_generator, varied_password_sizes):
        """
        Valida que cada uma das 50 senhas contém pelo menos:
        - 1 maiúscula (A-Z)
        - 1 minúscula (a-z)
        - 1 dígito (0-9)
        - 1 caractere especial
        """
        for password_size in varied_password_sizes:
            password = password_generator.generate(password_size)

            has_uppercase = any(c.isupper() for c in password)
            has_lowercase = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(not c.isalnum() for c in password)

            assert has_uppercase, f"Senha '{password}' não contém maiúscula"
            assert has_lowercase, f"Senha '{password}' não contém minúscula"
            assert has_digit, f"Senha '{password}' não contém dígito"
            assert has_special, f"Senha '{password}' não contém caractere especial"

    def test_all_50_passwords_are_unique_per_size(self, password_generator, varied_password_sizes):
        """
        Valida que senhas geradas no mesmo tamanho são diferentes entre si.
        (Para cada tamanho, temos 2 senhas, elas devem ser diferentes)
        """
        passwords_by_size = {}

        for password_size in varied_password_sizes:
            if password_size not in passwords_by_size:
                passwords_by_size[password_size] = []

            password = password_generator.generate(password_size)
            passwords_by_size[password_size].append(password)

        # Validar unicidade por tamanho
        for size, passwords in passwords_by_size.items():
            unique_passwords = set(passwords)
            assert len(unique_passwords) == len(passwords), \
                f"Senhas de tamanho {size} não são únicas: {passwords}"

    @pytest.mark.parametrize("password_length", [8, 10, 12, 15, 20, 25, 30])
    def test_password_entropy_for_varied_sizes(self, password_generator, password_length):
        """
        Testa que senhas de diferentes tamanhos têm boa entropia (diversidade de caracteres).
        Paramétrico: testa tamanhos 8, 10, 12, 15, 20, 25, 30.
        """
        password = password_generator.generate(password_length)

        # Calcular número de caracteres únicos (proxy para entropia)
        unique_chars = len(set(password))

        # Senhas com boa entropia devem ter pelo menos 60% de caracteres únicos
        entropy_ratio = unique_chars / password_length
        assert entropy_ratio >= 0.6, \
            f"Entropia baixa: apenas {unique_chars}/{password_length} chars únicos"

    def test_suggester_generates_50_distinct_suggestions_across_multiple_calls(self, password_suggester):
        """
        Valida que o sugestor pode gerar 50 sugestões distintas em múltiplas chamadas.
        """
        all_suggestions = []

        for _ in range(17):  # 17 * 3 = 51 sugestões
            suggestions = password_suggester.suggest(length=12, count=3)
            all_suggestions.extend(suggestions)

        # Pegar as 50 primeiras
        all_suggestions = all_suggestions[:50]

        # Validar que todas são únicas
        unique_suggestions = set(all_suggestions)
        assert len(unique_suggestions) == 50, \
            f"Apenas {len(unique_suggestions)} sugestões únicas de 50"

    def test_password_no_sequential_characters(self, password_generator):
        """Valida que senhas não contêm sequências previsíveis (ABC, 123, etc)."""
        for _ in range(10):
            password = password_generator.generate(12)

            # Verificar sequências previsíveis: 123, 234, 345, etc
            has_sequential_numbers = any(
                password[i:i+3] in 
                ['012', '123', '234', '345', '456', '567', '678', '789']
                for i in range(len(password) - 2)
            )
            
            # Verificar sequências previsíveis de letras: ABC, DEF, etc
            has_sequential_letters = any(
                password[i:i+3].upper() in 
                ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZ']
                for i in range(len(password) - 2)
            )

            # Não deve conter sequências previsíveis
            assert not (has_sequential_numbers or has_sequential_letters), \
                f"Senha '{password}' contém padrão sequencial previsível"

    def test_generator_with_selective_categories(self, varied_password_sizes):
        """
        Testa geradores com diferentes combinações de categorias de caracteres.
        Valida que cada combinação gera senhas válidas para múltiplos tamanhos.
        """
        # Combinações: (upper, lower, digit, special)
        combinations = [
            (True, True, False, False),   # Apenas letras
            (True, False, True, False),   # Maiúscula + dígito
            (False, True, True, True),    # Minúscula + dígito + especial
            (True, True, True, False),    # Maiúscula + minúscula + dígito
        ]

        for upper, lower, digit, special in combinations:
            generator = PasswordGenerator(
                include_upper=upper,
                include_lower=lower,
                include_digits=digit,
                include_punctuation=special
            )

            # Gerar senhas com alguns tamanhos variados
            for size in [8, 12, 20]:
                password = generator.generate(size)
                assert len(password) == size, \
                    f"Tamanho incorreto para combinação ({upper}, {lower}, {digit}, {special})"

    def test_minimum_and_maximum_size_consistency(self, password_generator):
        """
        Testa que o gerador funciona consistentemente nos limites mínimo (8) e máximo (30).
        """
        # Gerar 10 senhas de tamanho mínimo
        min_passwords = [password_generator.generate(8) for _ in range(10)]
        assert all(len(p) == 8 for p in min_passwords), "Senhas mínimas com tamanho incorreto"

        # Gerar 10 senhas de tamanho máximo
        max_passwords = [password_generator.generate(30) for _ in range(10)]
        assert all(len(p) == 30 for p in max_passwords), "Senhas máximas com tamanho incorreto"

        # Validar complexidade
        for password in min_passwords + max_passwords:
            has_categories = (
                any(c.isupper() for c in password) and
                any(c.islower() for c in password) and
                any(c.isdigit() for c in password) and
                any(not c.isalnum() for c in password)
            )
            assert has_categories, f"Senha não atende critérios mínimos: {password}"

    def test_50_passwords_performance(self, password_generator, varied_password_sizes):
        """
        Testa que 50 senhas podem ser geradas em tempo aceitável.
        Não falha se for rápido, apenas registra performance.
        """
        import time

        start_time = time.time()

        for password_size in varied_password_sizes:
            password_generator.generate(password_size)

        elapsed_time = time.time() - start_time

        # Deve gerar 50 senhas em menos de 1 segundo
        assert elapsed_time < 1.0, \
            f"Performance ruim: {elapsed_time:.3f}s para gerar 50 senhas"

        print(f"\n⚡ Gerou 50 senhas em {elapsed_time:.4f}s")

    def test_password_strength_distribution(self, password_generator):
        """
        Valida que senhas de diferentes tamanhos têm força proporcional ao tamanho.
        Força = número de chars únicos / tamanho da senha.
        """
        strength_scores = []

        for size in range(8, 31):  # 8 a 30
            password = password_generator.generate(size)
            unique_chars = len(set(password))
            strength = unique_chars / size
            strength_scores.append(strength)

        # Força média deve ser > 0.65
        average_strength = sum(strength_scores) / len(strength_scores)
        assert average_strength > 0.65, \
            f"Força média baixa: {average_strength:.2f}"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
