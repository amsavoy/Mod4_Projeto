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
      python -m venv .venv
     .\venv\Scripts\Activate.ps1
     pip install -r requirements.txt
     ```
   - No Linux/Mac:
     ```
     source .venv/bin/activate
     ```

3. **Execute o script principal**:
   ```
   python app/main.py or
   python -m app.main
   ```

   Substitua `app/main.py` pelo caminho do arquivo principal se necessário.

## Roadmap de Releases

- **v1.0 (Atual)**: Geração básica de senhas com comprimento fixo e caracteres mistos.
- **v1.1**: Adição de opções personalizáveis (comprimento, tipos de caracteres incluídos/excluídos).
- **v1.2**: Interface de linha de comando (CLI) aprimorada com argumentos.
- **v1.3**: Suporte a geração em lote e exportação para arquivo.
- **v2.0**: Interface gráfica simples (GUI) usando Tkinter ou similar.
- **Futuro**: Integração com gerenciadores de senhas e APIs para validação de força.

## Checklist de Reprodutibilidade em Máquina Limpa

- [ ] Documentar e usar um ambiente virtual local consistente: `python -m venv .venv`
- [ ] Incluir instruções de instalação de dependências com `pip install -r requirements.txt`
- [ ] Corrigir o comando de ativação do ambiente Windows para `./.venv/Scripts/Activate.ps1`
- [ ] Adicionar instrução para instalar `pytest` ou rodar testes via `python -m pytest`
- [ ] Explicar claramente como executar o app: `python -m app.main`

## Checklist de Onboarding Técnico

- [ ] Adicionar seção breve sobre a estrutura do projeto e principais arquivos (`app/main.py`, `app/storage.py`, `tests/`)
- [ ] Incluir como rodar os testes e o que cada suíte cobre
- [ ] Explicar a convenção de commits utilizada (por exemplo, Conventional Commits)
- [ ] Documentar como o histórico de senhas é salvo e onde o armazenamento está localizado
- [ ] Incluir um exemplo de comando completo de clonagem, setup e execução

## Checklist de Uso da IA

- [ ] Incluir uma seção dedicada ao uso de IA, se aplicável ao projeto
- [ ] Descrever quais prompts ou tipos de assistência são esperados
- [ ] Incluir exemplos de uso da IA para geração de testes, commits ou documentação
- [ ] Explicar limitações e contexto necessários para o agente responder corretamente
