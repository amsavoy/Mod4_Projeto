import pytest
import tempfile
from pathlib import Path
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'app'))

from storage import PasswordStorage


class TestPasswordStorage:
    """Testes para persistência de senhas."""

    @pytest.fixture
    def temp_storage(self):
        """Cria um storage temporário para testes."""
        with tempfile.TemporaryDirectory() as tmpdir:
            storage_path = Path(tmpdir) / "test_history.json"
            yield PasswordStorage(str(storage_path))

    def test_storage_initialization(self, temp_storage):
        """Deve criar arquivo ao inicializar."""
        assert temp_storage.storage_path.exists()

    def test_save_password(self, temp_storage):
        """Deve salvar uma senha com sucesso."""
        temp_storage.save_password("TestPass123!", 12)
        history = temp_storage.load_history()
        assert len(history) == 1
        assert history[0]['password'] == "TestPass123!"
        assert history[0]['length'] == 12

    def test_save_multiple_passwords(self, temp_storage):
        """Deve salvar múltiplas senhas."""
        temp_storage.save_password("Pass1", 8)
        temp_storage.save_password("Pass2", 15)
        temp_storage.save_password("Pass3", 20)
        
        history = temp_storage.load_history()
        assert len(history) == 3

    def test_load_history_with_limit(self, temp_storage):
        """Deve respeitar o limite ao carregar histórico."""
        for i in range(15):
            temp_storage.save_password(f"Pass{i}", 12)
        
        history = temp_storage.load_history(limit=5)
        assert len(history) == 5

    def test_clear_history(self, temp_storage):
        """Deve limpar todo o histórico."""
        temp_storage.save_password("Pass1", 12)
        temp_storage.save_password("Pass2", 12)
        
        assert len(temp_storage.load_history()) == 2
        
        temp_storage.clear_history()
        assert len(temp_storage.load_history()) == 0

    def test_timestamp_is_stored(self, temp_storage):
        """Deve armazenar timestamp ISO ao salvar."""
        temp_storage.save_password("Pass123", 12)
        history = temp_storage.load_history()
        
        assert 'timestamp' in history[0]
        assert 'T' in history[0]['timestamp']  # Formato ISO

    def test_get_storage_path(self, temp_storage):
        """Deve retornar o caminho do storage."""
        path = temp_storage.get_storage_path()
        assert path == str(temp_storage.storage_path)

    def test_empty_history_returns_empty_list(self, temp_storage):
        """Deve retornar lista vazia quando não há histórico."""
        history = temp_storage.load_history()
        assert history == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
