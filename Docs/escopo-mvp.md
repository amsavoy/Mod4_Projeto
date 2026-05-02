# Escopo - MVP Gerador de Senhas Complexas

## Objetivo

Fornecer uma ferramenta de linha de comando (CLI) para gerar senhas aleatórias e complexas, com configurações customizáveis de comprimento e tipos de caracteres, visando melhorar a segurança de credenciais através de combinações criptograficamente seguras.

## Requisitos Funcionais

- **RF-001**: Gerar senha aleatória com comprimento padrão de 12 caracteres
- **RF-002**: Permitir customização do comprimento da senha (intervalo: 8-30 caracteres)
- **RF-003**: Gerar senha composta por letras maiúsculas (A-Z), letras minúsculas (a-z), dígitos (0-9) e caracteres especiais
- **RF-004**: Permitir inclusão/exclusão de letras maiúsculas (A-Z)
- **RF-005**: Permitir inclusão/exclusão de letras minúsculas (a-z)
- **RF-006**: Permitir inclusão/exclusão de dígitos (0-9)
- **RF-007**: Permitir inclusão/exclusão de caracteres especiais (pontuação)
- **RF-008**: Exibir a senha gerada no terminal
- **RF-009**: Validar que pelo menos um tipo de caractere foi selecionado
- **RF-010**: Lançar exceção clara se todos os tipos de caracteres forem desabilitados
- **RF-007**: Exibir a senha gerada no terminal
- **RF-008**: Validar que pelo menos um tipo de caractere foi selecionado
- **RF-009**: Lançar exceção clara se todos os tipos de caracteres forem desabilitados

## Requisitos Não Funcionais

- **RNF-001**: Utilizar `secrets` module para geração criptograficamente segura
- **RNF-002**: Implementar tipagem estática (type hints) em toda a codebase
- **RNF-003**: Tempo de resposta < 100ms para senhas até 30 caracteres
- **RNF-004**: Compatibilidade com Python 3.11+
- **RNF-005**: Sem dependências externas (apenas stdlib)
- **RNF-006**: Código deve seguir PEP 8
- **RNF-007**: Documentação inline (docstrings) para todas as funções

## Fora de Escopo

- ❌ Interface gráfica (GUI)
- ❌ API REST/HTTP
- ❌ Persistência em banco de dados
- ❌ Sincronização em nuvem
- ❌ Importação/exportação de senhas
- ❌ Verificação de força da senha (força score)
- ❌ Rate limiting ou proteção contra força bruta
- ❌ Integração com gerenciadores de senhas
- ❌ Suporte a múltiplos idiomas
- ❌ Interface com argumentos CLI avançados (será v1.1+)