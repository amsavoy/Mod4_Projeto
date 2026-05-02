# Backlog - MVP Gerador de Senhas Complexas

## Release 1: Core (v1.0)

### RF-001: Gerar senha com comprimento padrão
- [ ] Implementar função `generate_password()` com comprimento padrão de 12 caracteres
- [ ] Aceita critério: Função retorna string com exatamente 12 caracteres
- [ ] Aceita critério: Caracteres incluem maiúsculas, minúsculas, dígitos e pontuação
- [ ] Aceita critério: Duas chamadas consecutivas geram senhas diferentes

### RF-002: Customizar comprimento da senha
- [ ] Adicionar parâmetro `length` à função `generate_password()`
- [ ] Aceita critério: Aceita comprimentos de 8 a 30 caracteres
- [ ] Aceita critério: Retorna string com comprimento exato solicitado
- [ ] Aceita critério: Validar e rejeitar comprimentos fora do intervalo permitido

### RF-003 a RF-006: Controlar tipos de caracteres
- [ ] Adicionar parâmetros `include_upper`, `include_lower`, `include_digits`, `include_punctuation`
- [ ] Aceita critério: Cada parâmetro pode ser habilitado/desabilitado independentemente
- [ ] Aceita critério: Senha contém apenas tipos de caracteres habilitados
- [ ] Aceita critério: Senha padrão inclui letras maiúsculas, minúsculas, dígitos e pontuação
- [ ] Aceita critério: Senhas parecem aleatórias (distribuição uniforme)

### RF-007: Exibir senha no terminal
- [ ] Implementar função `main()` que chama `generate_password()` e imprime resultado
- [ ] Aceita critério: Senha é exibida com prefixo claro ("Senha gerada: ")
- [ ] Aceita critério: Programa executa com `python app/main.py`

### RF-008 e RF-009: Validação de caracteres
- [ ] Validar que pelo menos um tipo de caractere está habilitado
- [ ] Aceita critério: Lança `ValueError` com mensagem clara se todos forem desabilitados
- [ ] Aceita critério: Mensagem indica qual tipo de caractere deve ser selecionado

---

## Release 2: Qualidade (v1.1)

### RT-001: Testes unitários - casos normais
- [ ] Criar suite de testes para `generate_password()` com valores padrão
- [ ] Aceita critério: Teste valida comprimento retornado (12 caracteres)
- [ ] Aceita critério: Teste valida presença de todos os tipos de caracteres
- [ ] Aceita critério: 100% de cobertura da função `generate_password()`

### RT-002: Testes unitários - casos limite
- [ ] Teste com `length=8`
- [ ] Teste com `length=30`
- [ ] Teste com `length=0` (deve falhar)
- [ ] Teste com `length=-5` (deve falhar)
- [ ] Aceita critério: Todos os casos limite retornam comportamento esperado

### RT-003: Testes unitários - combinações de caracteres
- [ ] Teste com apenas maiúsculas
- [ ] Teste com apenas minúsculas
- [ ] Teste com apenas dígitos
- [ ] Teste com apenas pontuação
- [ ] Teste com nenhum tipo habilitado (deve lançar `ValueError`)
- [ ] Aceita critério: Todas as combinações geram senhas corretas

### RT-004: Testes de aleatoriedade
- [ ] Gerar 1000 senhas e validar que nenhuma é duplicada
- [ ] Aceita critério: Taxa de duplicação < 0.1%
- [ ] Aceita critério: Distribuição de caracteres é uniforme

### RT-005: Testes de performance
- [ ] Medir tempo de geração para `length=30`
- [ ] Aceita critério: Tempo de execução < 100ms
- [ ] Aceita critério: Consumo de memória < 1MB

### RT-006: Cobertura de testes
- [ ] Atingir 85%+ de cobertura de código
- [ ] Aceita critério: Todos os paths de erro cobertos
- [ ] Aceita critério: Todas as branches testadas

---

## Release 3: Final (v1.2)

### RF-010: Argumentos CLI básicos
- [ ] Implementar argumentos de linha de comando com `argparse`
- [ ] Aceita critério: `--length` permite definir comprimento
- [ ] Aceita critério: `--no-upper` desabilita maiúsculas
- [ ] Aceita critério: `--no-lower` desabilita minúsculas
- [ ] Aceita critério: `--no-digits` desabilita dígitos
- [ ] Aceita critério: `--no-punct` desabilita pontuação
- [ ] Aceita critério: `--help` exibe documentação clara

### RF-011: Múltiplas gerações
- [ ] Adicionar argumento `--count` para gerar múltiplas senhas
- [ ] Aceita critério: Gera N senhas (padrão: 1)
- [ ] Aceita critério: Cada senha é exibida em linha separada
- [ ] Aceita critério: Exibe contador (Senha 1/N, Senha 2/N, etc.)

### RT-007: Testes de integração
- [ ] Testar CLI com diferentes argumentos
- [ ] Aceita critério: Todos os argumentos funcionam corretamente
- [ ] Aceita critério: Help message exibido sem erros

### NF-001: Documentação e qualidade
- [ ] Adicionar docstrings completas em todas as funções
- [ ] Aceita critério: Docstrings seguem padrão Google/NumPy
- [ ] Aceita critério: README atualizado com exemplos de uso
- [ ] Aceita critério: Código passa em linter (pylint/flake8)

### NF-002: Preparação para produção
- [ ] Criar `setup.py` para facilitar instalação
- [ ] Aceita critério: Pacote instalável com `pip install -e .`
- [ ] Aceita critério: Executável `password-generator` disponível após instalação
- [ ] Aceita critério: Versão definida em `__version__`