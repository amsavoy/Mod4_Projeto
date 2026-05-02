# Roteiro de Apresentação do MVP

## Objetivo
Apresentar o MVP do gerador de senhas para stakeholders técnicos em 5 minutos, com foco em demonstração prática e pontos de valor técnico.

## Estrutura do tempo

1. **00:00 - 00:45 | Contexto rápido**
   - Descrever em uma frase o que o MVP faz: gerador de senhas complexas com critérios de segurança.
   - Explicar o problema que resolve: senhas fracas e necessidade de geração segura.

2. **00:45 - 02:15 | Arquitetura e código**
   - Mostrar brevemente a estrutura do projeto:
     - `app/main.py` - interface de linha de comando simples
     - `app/storage.py` - persistência de histórico
     - `tests/` - cobertura de qualidade
   - Destacar a separação entre geração, validação e armazenamento.

3. **02:15 - 03:30 | Demonstração no terminal**
   - Executar o aplicativo:
     ```powershell
     python -m app.main
     ```
   - Gerar senhas com opção `1` e comprimento `12`.
   - Mostrar histórico com opção `2`.

4. **03:30 - 04:15 | Qualidade e testes**
   - Citar que há testes automatizados e que uma suite foi adicionada para 50 senhas variáveis.
   - Comando para rodar testes:
     ```powershell
     python -m pytest tests/test_task_service.py -v
     ```

5. **04:15 - 05:00 | Próximos passos técnicos**
   - Apontar melhorias factíveis:
     - CLI com argumentos
     - geração em lote
     - exportação de histórico
     - integração com gerenciadores de senha
   - Finalizar com o estado atual: funcional e pronto para iteração rápida.
