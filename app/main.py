import random
import secrets
import string
from typing import Optional

from storage import PasswordStorage

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 30



class PasswordValidator:
    """Valida requisitos de senha."""

    @staticmethod
    def validate_length(length: int) -> None:
        """Valida se o comprimento está dentro dos limites permitidos."""
        if length < MIN_PASSWORD_LENGTH or length > MAX_PASSWORD_LENGTH:
            raise ValueError(
                f"Comprimento deve estar entre {MIN_PASSWORD_LENGTH} e {MAX_PASSWORD_LENGTH}."
            )

    @staticmethod
    def validate_categories(include_upper: bool, include_lower: bool,
                           include_digits: bool, include_punctuation: bool) -> None:
        """Valida se pelo menos uma categoria de caracteres foi selecionada."""
        if not (include_upper or include_lower or include_digits or include_punctuation):
            raise ValueError("Selecione pelo menos uma categoria de caracteres.")


class PasswordGenerator:
    """Gera senhas complexas e seguras."""

    def __init__(self, include_upper: bool = True, include_lower: bool = True,
                 include_digits: bool = True, include_punctuation: bool = True):
        """Inicializa o gerador com categorias de caracteres."""
        PasswordValidator.validate_categories(include_upper, include_lower, include_digits, include_punctuation)
        self.include_upper = include_upper
        self.include_lower = include_lower
        self.include_digits = include_digits
        self.include_punctuation = include_punctuation

    def generate(self, length: int) -> str:
        """Gera uma senha segura com o comprimento especificado."""
        PasswordValidator.validate_length(length)

        categories: list[str] = []
        required_chars: list[str] = []

        if self.include_upper:
            categories.append(string.ascii_uppercase)
            required_chars.append(secrets.choice(string.ascii_uppercase))
        if self.include_lower:
            categories.append(string.ascii_lowercase)
            required_chars.append(secrets.choice(string.ascii_lowercase))
        if self.include_digits:
            categories.append(string.digits)
            required_chars.append(secrets.choice(string.digits))
        if self.include_punctuation:
            categories.append(string.punctuation)
            required_chars.append(secrets.choice(string.punctuation))

        if length < len(required_chars):
            raise ValueError("Comprimento insuficiente para todas as categorias.")

        pool = ''.join(categories)
        password_chars = required_chars + [secrets.choice(pool) for _ in range(length - len(required_chars))]
        random.SystemRandom().shuffle(password_chars)

        return ''.join(password_chars)


class PasswordSuggester:
    """Sugere múltiplas senhas distintas."""

    def __init__(self, generator: PasswordGenerator):
        """Inicializa com um gerador de senhas."""
        self.generator = generator

    def suggest(self, length: int, count: int = 3) -> list[str]:
        """Gera múltiplas sugestões de senhas distintas."""
        suggestions: set[str] = set()
        while len(suggestions) < count:
            suggestions.add(self.generator.generate(length))
        return sorted(list(suggestions))


def get_password_length() -> int:
    """Obtém o comprimento da senha do usuário com validação."""
    while True:
        try:
            length = int(input(f"\nDigite o comprimento da senha ({MIN_PASSWORD_LENGTH}-{MAX_PASSWORD_LENGTH}): "))
            PasswordValidator.validate_length(length)
            return length
        except ValueError as e:
            print(f"❌ Erro: {e}")


def show_menu() -> str:
    """Exibe menu de opções e retorna a escolha do usuário."""
    print("\n" + "=" * 50)
    print("Menu Principal")
    print("=" * 50)
    print("1. Gerar senhas")
    print("2. Ver histórico")
    print("3. Limpar histórico")
    print("0. Sair")
    print("=" * 50)
    return input("Escolha uma opção (0-3): ").strip()


def show_history(storage: PasswordStorage) -> None:
    """Exibe histórico de senhas geradas."""
    history = storage.load_history(limit=20)
    if not history:
        print("\n📋 Histórico vazio.")
        return
    
    print("\n📋 Últimas senhas geradas:")
    for i, entry in enumerate(history, 1):
        timestamp = entry.get('timestamp', 'N/A')[:19]
        password = entry.get('password', 'N/A')
        length = entry.get('length', 'N/A')
        print(f"  {i}. {password} ({length} chars) - {timestamp}")


def generate_passwords_flow(storage: PasswordStorage) -> None:
    """Fluxo de geração de senhas."""
    try:
        length = get_password_length()
        generator = PasswordGenerator()
        suggester = PasswordSuggester(generator)
        suggestions = suggester.suggest(length, count=3)

        print(f"\n✅ Sugestões de senhas ({length} caracteres):\n")
        for i, password in enumerate(suggestions, 1):
            print(f"  {i}. {password}")
            storage.save_password(password, length)
        print()

    except ValueError as e:
        print(f"❌ Erro: {e}")


def main() -> None:
    """Função principal - interface console do gerador de senhas."""
    storage = PasswordStorage()
    
    print("=" * 50)
    print("🔐 Gerador de Senhas Complexas")
    print("=" * 50)

    try:
        while True:
            choice = show_menu()
            
            if choice == "1":
                generate_passwords_flow(storage)
            elif choice == "2":
                show_history(storage)
            elif choice == "3":
                confirm = input("\n⚠️ Tem certeza? Digite 'sim' para confirmar: ").strip().lower()
                if confirm == "sim":
                    storage.clear_history()
                    print("✅ Histórico limpo.")
            elif choice == "0":
                print("\n👋 Até logo!")
                break
            else:
                print("❌ Opção inválida.")

    except KeyboardInterrupt:
        print("\n\n⛔ Operação cancelada pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")


if __name__ == "__main__":
    main()