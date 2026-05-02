# Initial Project Analysis

## 1. Riscos Técnicos

- [ ] **Validação de `length`**: Aceita valores negativos ou zero sem validar
- [ ] **Recursos**: Valor muito alto de `length` pode consumir memória excessiva
- [ ] **Caracteres especiais**: `string.punctuation` pode incluir caracteres não suportados em certos sistemas
- [ ] **Consistência de encoding**: Sem validação de compatibilidade com Unicode/ASCII
- [ ] **Segurança**: Usar `secrets` é correto, mas não há rate limiting ou proteção contra força bruta

## 2. O Que Quebra em Produção

- [ ] **Length inválido**: `length <= 0` causará erro ou resultado vazio
- [ ] **Sem caracteres**: Se todas as opções forem `False`, levanta `ValueError`
- [ ] **Performance**: Geração com `length > 1.000.000` pode travar o programa
- [ ] **Pontuação incompatível**: Alguns caracteres em `string.punctuation` podem não ser aceitos por APIs/sistemas
- [ ] **Sem tratamento de exceção**: Função `main()` não captura erros

## 3. Testes Mínimos

- [ ] Teste geração com valores padrão (12 caracteres)
- [ ] Teste com `length=0` (deve falhar ou retornar vazio)
- [ ] Teste com `length=-5` (deve falhar)
- [ ] Teste com `length=30` (performance)
- [ ] Teste com todas as opções `False` (deve lançar `ValueError`)
- [ ] Teste combinações de tipos de caracteres (apenas maiúsculas, apenas dígitos, etc.)
- [ ] Teste comprimento da senha gerada (validar exatamente `length` caracteres)
- [ ] Teste aleatoriedade (duas chamadas devem gerar senhas diferentes)
- [ ] Teste presença de tipos de caracteres esperados na senha gerada
- [ ] Teste `requirements.txt` para instalar dependências (se houver)