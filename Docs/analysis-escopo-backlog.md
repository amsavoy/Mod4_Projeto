# Análise de Escopo e Backlog

## 1) O que está grande demais para a release inicial?
- [ ] RT-004: testar 1000 senhas para aleatoriedade é mais adequado à fase de qualidade do que ao core
- [ ] RT-006: exigir 85%+ de cobertura no MVP pode atrasar a entrega inicial
- [ ] RF-010/RF-011 CLI avançado deve ficar para release seguinte, não para o core

## 2) O que está faltando para testabilidade?
- [ ] Definição de casos de teste para a interface de execução `python app/main.py`
- [ ] Testes de erro para entradas inválidas de `length` e parâmetros de categoria
- [ ] Critérios claros para validar saída de terminal e formato da senha

## 3) Quais 3 riscos técnicos devo mitigar antes da implementação?
- [ ] Validação de comprimento e tipos de caractere para não gerar senha inválida ou sem categorias
- [ ] Compatibilidade de caracteres especiais no terminal e em sistemas de destino
- [ ] Dependência de `secrets`/random: garantir que a senha contenha todos os tipos habilitados e não apenas pool aleatório
