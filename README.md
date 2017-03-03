# MUNICIPIOS #

## Visao geral

Este programa permite cadastrar e buscar os municipios
do estado de Minas Gerais em uma base de dados SQLite.

O programa e dividido em dois arquivos principais:

* extracao.py - Arquivo responsável por gerar a base dados dos municipios.
* municipios.py - Programa que executa um servidor que pode ser acessado via web para pesquisa.

## Instalação

Para instalar as dependências para funcionamento da aplicação
basta utilizar o gerenciador de pacotes PIP com
o arquivo **requirements.txt**:

pip install -r requirements.txt

### Dependencias

Segue abaixo a lista completa de dependências da aplicação.
Apenas o pacote **Flask** deve ser instalado, já que os
demais acompanham a distribuição padrão do Python:

* flask - Framework para desenvolvimento REST
* sqlite3 - Banco de dados
* json - Manipulacoa de dados em formato JSON
* urllib - Biblioteca para realizacao de consultas HTTP
* ssl - Configuracao e manupulacao de propriedades do protocolo SSL

### Executando

Para executar o programa é necessário primeiramente executar
o arquivo **extracao.py**. Exemplo:

> python extracao.py

Quando executado, este arquivo ira criar uma base de dados
SQLite no mesmo diretorio, acessar a API com as informacoes
dos municipios, e salvar todas elas na tabela para que os
dados possam ser consultados.

Uma vez extraidas as informacoes da API, a busca pelas informacoes
pode ser feita executando o arquivo **app.py**. Exemplo:

> python app.py

Ao fazer isso um webserver sera executado no endereco
**http://localhost:5000** (importante indicar o protocolo HTTP).
Agora basta utilizar seu para acessar o endereco indicado.

## Detalhes da busca

A página de busca fornece um único campo de texto para
realizacao das consultas. Este campo lhe dá duas opções de busca:

* Digitar um número do IBGE irá buscar um municipio por este número.
* Digitar uma palavra irá buscar as cidades que possuam no nome a palavra indicada.
