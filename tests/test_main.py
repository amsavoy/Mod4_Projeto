import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'app'))

from main import PasswordValidator, PasswordGenerator, PasswordSuggester


class TestPasswordValidator:
    """Testes para validação de requisitos."""

    def test_valid_length(self):
        """Deve aceitar comprimentos entre 8 e 30."""
        PasswordValidator.validate_length(8)
        PasswordValidator.validate_length(15)
        PasswordValidator.validate_length(30)

    def test_invalid_length_too_small(self):
        """Deve rejeitar comprimento < 8."""
        with pytest.raises(ValueError, match="entre 8 e 30"):
            PasswordValidator.validate_length(7)

    def test_invalid_length_too_large(self):
        """Deve rejeitar comprimento > 30."""
        with pytest.raises(ValueError, match="entre 8 e 30"):
            PasswordValidator.validate_length(31)

    def test_at_least_one_category(self):
        """Deve rejeitar se nenhuma categoria foi selecionada."""
        with pytest.raises(ValueError, match="Selecione pelo menos"):
            PasswordValidator.validate_categories(False, False, False, False)


class TestPasswordGenerator:
    """Testes para geração de senhas."""

    def test_default_password_length(self):
        """Senha gerada deve ter o comprimento exato solicitado."""
        gen = PasswordGenerator()
        pwd = gen.generate(12)
        assert len(pwd) == 12

    def test_password_contains_required_categories(self):
        """Senha padrão deve conter maiúsculas, minúsculas, dígitos e especiais."""
        gen = PasswordGenerator()
        pwd = gen.generate(20)
        
        has_upper = any(c.isupper() for c in pwd)
        has_lower = any(c.islower() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(not c.isalnum() for c in pwd)
        
        assert has_upper and has_lower and has_digit and has_special

    def test_different_passwords_on_consecutive_calls(self):
        """Duas chamadas consecutivas devem gerar senhas diferentes."""
        gen = PasswordGenerator()
        pwd1 = gen.generate(12)
        pwd2 = gen.generate(12)
        assert pwd1 != pwd2

    def test_only_uppercase(self):
        """Gerar senha apenas com maiúsculas."""
        gen = PasswordGenerator(include_upper=True, include_lower=False, 
                               include_digits=False, include_punctuation=False)
        pwd = gen.generate(10)
        assert pwd.isupper()

    def test_minimum_length(self):
        """Deve gerar senha com comprimento mínimo permitido."""
        gen = PasswordGenerator()
        pwd = gen.generate(8)
        assert len(pwd) == 8

    def test_maximum_length(self):
        """Deve gerar senha com comprimento máximo permitido."""
        gen = PasswordGenerator()
        pwd = gen.generate(30)
        assert len(pwd) == 30


class TestPasswordSuggester:
    """Testes para sugestões de senhas."""

    def test_suggest_three_distinct_passwords(self):
        """Deve gerar 3 sugestões de senhas distintas."""
        gen = PasswordGenerator()
        sugg = PasswordSuggester(gen)
        passwords = sugg.suggest(12, count=3)
        
        assert len(passwords) == 3
        assert len(set(passwords)) == 3  # todas distintas

    def test_all_suggestions_have_correct_length(self):
        """Todas as sugestões devem ter o comprimento solicitado."""
        gen = PasswordGenerator()
        sugg = PasswordSuggester(gen)
        passwords = sugg.suggest(15, count=3)
        
        for pwd in passwords:
            assert len(pwd) == 15

    def test_suggest_returns_sorted_list(self):
        """Sugestões devem retornar em ordem alfabética."""
        gen = PasswordGenerator()
        sugg = PasswordSuggester(gen)
        passwords = sugg.suggest(12, count=3)
        
        assert passwords == sorted(passwords)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
