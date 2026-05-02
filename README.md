# Gerador de Senhas Complexas - MVP

## Objetivo

Este MVP oferece uma ferramenta simples para gerar senhas complexas, visando melhorar a segurança de contas e sistemas através de combinações aleatórias de caracteres.

## Stack Tecnológica

- **Linguagem**: Python 3.11+
- **Ambiente Virtual**: .venv (para isolamento de dependências)
- **Versionamento**: Git

## Requisitos de Senha

- Comprimento mínimo: 8 caracteres
- Comprimento máximo: 30 caracteres
- Conteúdo: letras maiúsculas, letras minúsculas, dígitos e caracteres especiais

## Como Rodar Localmente

1. **Clone o repositório** (se aplicável):
   ```
   git clone <url-do-repositorio>
   cd Mod4_Projeto
   ```

2. **Ative o ambiente virtual**:
   - No Windows (PowerShell):
     ```
     .\venv\Scripts\Activate.ps1
     ```
   - No Linux/Mac:
     ```
     source .venv/bin/activate
     ```

3. **Execute o script principal**:
   ```
   python app/main.py
   ```

   Substitua `app/main.py` pelo caminho do arquivo principal se necessário.

## Roadmap de Releases

- **v1.0 (Atual)**: Geração básica de senhas com comprimento fixo e caracteres mistos.
- **v1.1**: Adição de opções personalizáveis (comprimento, tipos de caracteres incluídos/excluídos).
- **v1.2**: Interface de linha de comando (CLI) aprimorada com argumentos.
- **v1.3**: Suporte a geração em lote e exportação para arquivo.
- **v2.0**: Interface gráfica simples (GUI) usando Tkinter ou similar.
- **Futuro**: Integração com gerenciadores de senhas e APIs para validação de força.