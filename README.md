## Aprendizados e Experiência

Durante o desenvolvimento deste projeto, explorei e aprendi diversos conceitos importantes:

- **Integração de IA em fluxos de desenvolvimento:** Entendi como é possível automatizar tarefas repetitivas de programação utilizando modelos de linguagem, economizando tempo e aumentando a confiabilidade dos testes.
- **LangChain + Azure OpenAI:** Tentei implementar a solução utilizando o Azure OpenAI, mas encontrei uma limitação no caso de ser apto a utilizar da azure marketplace e usar da OpenIA deles, já que seria necessário para utilizar a API de forma completa.
- **Descoberta do Ollama:** Durante minhas tentativas, conheci o **Ollama**, que permite rodar modelos de IA localmente. Isso abriu novas possibilidades para criar agentes offline sem depender de chamadas externas pagas.
- **Desenvolvimento de chatbots inteligentes:** Aprendi que é possível criar chatbots que resolvem problemas do dia a dia de forma integral, como a geração automática de testes unitários, validação de códigos, entre outros.

---

## Tentativas e Dificuldades

Minha primeira abordagem foi tentar implementar o agente usando **Azure OpenAI**, mas devido à necessidade de acesso ao marketplace, a execução completa não foi possível. Isso me levou a explorar alternativas locais, como o **Ollama**, onde descobri que é possível:

- Carregar modelos pré-treinados localmente;
- Integrar com Python para criar agentes de teste;
- Evitar custos extras e manter o desenvolvimento de forma autônoma.

Também enfrentei desafios ao gerar testes complexos automaticamente, como a criação de casos de falha para funções que envolvem tratamento de exceções e validações específicas.
