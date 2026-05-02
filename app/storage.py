import json
from datetime import datetime
from pathlib import Path
from typing import Optional


class PasswordStorage:
    """Gerencia persistência de senhas geradas em JSON."""

    def __init__(self, storage_path: Optional[str] = None):
        """Inicializa o storage com caminho do arquivo JSON."""
        if storage_path is None:
            storage_path = str(Path.home() / '.password_generator' / 'history.json')
        
        self.storage_path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """Cria diretório e arquivo se não existirem."""
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.storage_path.exists():
            self.storage_path.write_text(json.dumps([], indent=2))

    def save_password(self, password: str, length: int) -> None:
        """Salva uma senha gerada com timestamp."""
        try:
            history = self._load_history()
            entry = {
                'password': password,
                'length': length,
                'timestamp': datetime.now().isoformat()
            }
            history.append(entry)
            self.storage_path.write_text(json.dumps(history, indent=2))
        except Exception as e:
            print(f"⚠️ Aviso: Falha ao salvar histórico: {e}")

    def load_history(self, limit: int = 10) -> list[dict]:
        """Carrega últimas N senhas do histórico."""
        history = self._load_history()
        return history[-limit:] if history else []

    def clear_history(self) -> None:
        """Limpa todo o histórico de senhas."""
        try:
            self.storage_path.write_text(json.dumps([], indent=2))
        except Exception as e:
            print(f"⚠️ Aviso: Falha ao limpar histórico: {e}")

    def get_storage_path(self) -> str:
        """Retorna o caminho do arquivo de storage."""
        return str(self.storage_path)

    def _load_history(self) -> list[dict]:
        """Carrega histórico do arquivo JSON."""
        try:
            content = self.storage_path.read_text()
            return json.loads(content) if content else []
        except (json.JSONDecodeError, IOError):
            return []
