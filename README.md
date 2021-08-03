# webscraping

## Descrição
Webscraping para trackeamento de capital de preços diários (ou de hora em hora).

## Melhorias
- Realizar melhor o tratamento de exceções.
- Estruturar um pouco melhor a organização das pastas (criar uma pasta separando a classe do arquivo "main").
- Desacoplar o código um pouco mais (não deixando uma única classe responsável por executar todas as funções).
- Utilizaria algum orquestrador (como o Airflow) com GCP|AWS processando diáriamente ou de hora em hora (como sugerido).
- Utilizar o wedDriver manager para gerenciar automaticamente com problemas de versionamento do navegador.
- Atualmente o código está apto para rodar no final do dia (quando as cotações são encerradas). Porém, alterando algumas linhas de código, é possível rodar de hora em hora.
