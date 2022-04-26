# Resumo do Módulo 14: REST API com Django Rest Framework <h1>

# O que é uma API? <h3>
Application Programming Interface, ou Interface de Programação de Aplicações nada mais é do que um conjunto de definições
e protocolos para criar e integrar softwares e aplicações.

**HTTP API**

Expõe uma API através do protocolo HTTP

*POST /usuarios/1/* -> Retorna usuário com id 1

*POST /usuarios/* -> Retorna lista de usuário

*POST /criar_usuario/* -> Criar um novo usuário

*POST /deletar_usuario/1/* -> Deleta o  usuário com id 1

# REST API <h3>
Representational State Transfer, ou Transferência de um Estado Representacional, é um conjunto de restrições e um padrão
de arquitetura sobre como construir um API, ou seja, como expor operações para fazer manipulações do estado da aplicação
ou de recursos de uma aplicação. Recurso é por exemplo usuário.

# Padrões REST <h3>
A nossa API tem que seguir um conjunto de regras ou padrões, para ser considerada uma REST API:

* **Uniform Interface**

Identificação de um recurso usuário uniforme, utilizando o mesma representação */usuarios/1/* por exemplo, e diferentes operações como a *GET, DELETE, PUT, PATCH*.

* **Stateless**

Não tem preservação de estado entre requisições. Cada requisição é suficiente para realizar uma operação. Por exemplo, para *alterar* um usuário não é necessário *buscar* esse usuário antes.

* **Cacheable**

Definimos respostas que podem ser cacheadas, e não precisamos realizar a operação novamente.

* **Client-server**

Cliente seria o navegador Web e o servidor é separado, ou seja, não tem nada na máquina do cliente. Facilita a criação de diferentes clientes para a mesma aplicação.

# Protocolo HTTP != REST <h3>
O padrão de arquitetura REST não precisa ser implementado em HTTP, porém o protocolo HTTP atende muito bem o REST, com os métodos GET, PUT, PATCH, DELETE, POST..

# Protocolo JSON != HTTP <h3>
JSON é um dos formatos que podem ser utilizados para a representação e manipulação de recursos, porém acabou virando o padrão para aplicação Web.


Para saber mais a respeito 

<https://restfulapi.net/>

<https://developer.mozilla.org/pt-BR/docs/Glossary/REST>

# Configurando nosso Projeto <h2>
É recomendado iniciar o projeto do zero. Entre no diretório que queremos criar nosso projeto e execute os seguintes comandos:

*Cria pasta: mkdir "nome da pasta do projeto" -> entra na pasta: cd drf-api -> Cria o ambiente virtual dentro da pasta : python3 -m venv venv -> ativa o ambiente virtual: source venv/bin/activate -> instala o Django: pip install Django==4.0.2 -> instal o Django Rest Framework: pip install djangorestframework -> Cria o projeto Django colocando o ponto no final para criar os arquivos dentro dessa pasta e não dentro de outra pasta: django-admin startproject "nome do projeto" . -> Podemos abrir o VS Code através do comando 'code', caso esteja configurado no PATH do VSCode.*

Com o VSCode aberto, devemos selecionar o interpretador Python com o comando Shift+command+P e digitar interpretador python e selecionar o ambiente virtual recomendado. Pode-se observar que ao abrir o terminal com o comando control+` irá aparecer que está utilizando o nosso ambiente virtual. Estrutura que devemos ter no momento é manage.py, pasta com o nome do nosso projeto e a pasta do ambiente virtual. É interessante colocar a pasta venv no .gitignore, assim como os arquivos .sqlite3, pycache...

Dentro do terminal criamos um novo app com o comando django-admin startapp "nome do app" ,e será criado uma nova pasta com o nome do nosso app.