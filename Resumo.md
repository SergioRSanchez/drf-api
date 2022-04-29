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

Com o VSCode aberto, devemos selecionar o **interpretador** Python com o comando **Shift+command+P** e digitar *interpretador python* e selecionar o ambiente virtual recomendado. Pode-se observar que ao abrir o terminal com o **comando control+`** irá aparecer que está utilizando o nosso ambiente virtual. Estrutura que devemos ter no momento é **manage.py, pasta com o nome do nosso projeto e a pasta do ambiente virtual**. É interessante colocar a pasta venv no .gitignore, assim como os arquivos .sqlite3, pycache...

Dentro do terminal criamos um novo app com o comando *django-admin startapp "nome do app"* ,e será criado uma nova pasta com o nome do nosso app.

Vamos iniciar nosso repositório git com o comando git init. Lembrando que não temos um repositório de destino para esse git, nesse caso eu criei um novo repositório. Para enviar nosso push devemos digitar *git remote add origin url do repositório* -> entrar na branch main com o *git branch -M main* -> e dar o push para o main com o *git push -u origin main*. Pronto, nosso projeto está no GitHub.

Nosso projeto é criar um **Aplicativo de Agendamento**, no qual temos o administrador do serviço e os clientes, que fazem a requisição de um horário para determinado serviço.
# Regras de Negócios da nossa API <h2>
Nossa API terá os seguintes comandos:

- Listar agendamentos: `GET /agendamentos/`
- Detalhar agendamento: `GET /agendamentos/<id>/`
- Criar agendamento: `POST /agendamentos/`
- Excluir agendamento: `DELETE /agendamentos/<id>/`
- Editar agendamento parcialmente `PATCH /agendamentos/<id>/`
- Listar horarios: `GET /horarios/?data=YYYY-MM-DD`

Por enquanto não teremos diversos prestadores de serviço, somente um, o qual selecionamos o horário para o seu serviço. No próximo passo iremos criar nosso modelo de agendamentos.

# Modelando nosso Projeto <h2>
Entramos em *model.py* dentro do app *agenda* e criamos a classe Agendamento, lembrando que deve herdar da classe models.Model do django.db pois vai ser um modelo que vai ser criado no nosso banco de dados. Depois preenchemos com os campos que queremos em nosso banco de dados. Lembrando que se for *CharField* deve ser definido o *max_length*.

Depois de preencher nosso modelo, devemos fazer a migração e executar a migração. Para isso devemos adicionar o app **agenda** no nosso projeto **tamarcado**. Dentro da pasta *tamarcado* abrimos o arquivo *settings.py* e procuramos por *INSTALLED_APP* e adicionamos o app *'agenda'*. Depois basta rodar nossas migrações com o comando **python manage.py makemigrations**, será criado a pasta *migrate* e dentro dela o arquivo **0001_initial.py** que mostra que é nossa primeira migração. Para realmente efetuar a migração devemos rodar o comando **python manage.py migrate**. Pronto, modelo criado.

Agora vamos criar nossa **view**. Para isso devemos ter um arquivo **urls.py** dentro do app *agenda*. No arquivo *urls.py* dentro da pasta **tamarcado** devemos criar um novo *path* que é **'api/'**, que vai herdar de nosso **agenda.urls**, para isso usamos o comando *include* do *django.conf.urls*. Depois inserimos as *url patterns* dentro de *urls.py* do nosso app *agenda*. Lá colocamos os caminhos urls que iremos seguir quando chamarmos nossas *views*. Lembrando que essa *view* que falamos aqui por último é do app *agenda*, portando temos que importar de **agenda.views**.

No nosso arquivo **views.py** no app *agenda* iremos criar as funções que iremos chamar. Iremos fazer uma serialização do nosso objeto, que nada mais é que gerar uma representação textual desse objeto, nesse caso em formato Json, que reflete um dicionário no Python como por exemplo:
{
  "horario": 12:30,
  "nome": "Sergio"
}
Para isso criamos um arquivo **serializer.py** dentro do app *agenda*. Nele importamos a biblioteca **serializers** do **rest_framework** e criamos nossa classe AgendamentoSerializer, que será responsável por fazer a serialização dos objetos do tipo Agendamento. Nesse caso criamos uma relação 1 para 1 do nosso modelo, com os mesmo campos, pois queremos serializar (exibir) todos os atributos.

**O método que será implementado agora é o Function Based View, que não é o melhor método, porém fizemos para aprendizado de como funciona as coisas e está aqui documentado para eventuais consultas.**

Depois devemos ir na nossa *view* para fazer a serialização do nosso objeto. Para isso criamos um objeto serializer e passamos para ela uma instância, que no nosso caso é nosso objeto, que por sua vez é uma instância da classe Agendamento. Nesse momento o construtor do AgendamentoSerializer quando recebe o objeto ele vai tentar encontrar dentro desse objeto os campos que contêm os valores *data_horario, nome_cliente...*, por isso colocamos os mesmo nomes do nosso modelo no nosso serializer. Ou seja, esse objeto serializer vai ter um atributo **.data** que vai ser uma representação em formato dicionário do Python dos atributos do nosso objeto.

Para verificar se nossa aplicação está funcionando, executamos o comando **python manage.py runserver**. Quando executamos nosso servidor nesse momento, devemos seguir a url **/api/agendamentos/'id'**, porém vai dar um erro esperado, o **404 Page not found**, pois não temos nenhum agendamento criado ainda.

Para criar novos agendamentos, podemos utilizar o **shell** através do comando *python manage.py shell* ou então através do **django-admin**, lembrando que precisamos registrar o modelo em *admin.py*, para isso entramos no *admin.py* dentro do app *agenda*, importamos o modelo *Agendamento* e registramos com o comando *admin.site.register(Agendamento)*. Dessa forma podemos **adicionar, editar e deletar** posts que acabamos de modelar. Para fazer login precisamos criar um **superusuário (superuser)**, através do comando **python manage.py createsuperuser**. Será solicitado um username, que por padrão é o mesmo do sistema, um email e uma senha. Depois disso basta entrar no <http://127.0.0.1:8000/admin> e fazer login. Como este é um projeto de aprendizado, deixei o padrão do sistema e senha usei 12345.

Dessa maneira, podemos testar nossa view *agendamento_detail* através do <http://127.0.0.1:8000/api/agendamentos/id/> (no qual o id corresponde ao id de determinado agendamento), e essa view detalha um único agendamento de interesse.

Agora iremos implementar nosso *agendamento_list*, que consiste em uma **lista** com todos nosso agendamentos.

Para isso iremos no nosso arquivo *views.py* e criamo uma nova função *agendamento_list* que irá fazer uma **consulta** em todos nossos agendamentos. Se não fosse pelo Django teríamos que fazer toda a serialização, mas como estamos no Django iremos utilizar o *serializer*, passando o **queryset** como parâmetro (no lugar do obj que foi na outra vez), e o parâmetro **many=True** que é para serializar esse objeto como se fossem muitos. Por padrão uma *JsonResponse* só permite que retorne um objeto do tipo dicionário, mas o nosso *serializer.data* vai ser uma lista com dicionários, e para corrigir isso devemos passar o parâmetro **safe=False**. Podemos conferir através do link <http://127.0.0.1:8000/api/agendamentos/>, ou então configurar as requisições no Postman ou no Thunder Client de acordo com as especificações da nossa API.

# Decorator api_view<h2>
Quando tentamos utilizar nossa *agendamento_detail* com um *id* que não foi cadastrado ainda, ele está retornando um *Html*, e olhando no *Header* vemos que o *Content-Type* é *text/html*, ou seja, nossa API retorna um json só quando tudo dá certo, e gostaríamos que ela sempre retornasse um json, que ela fosse consistente. Poderíamos lidar manualmente com essa exceção, porém o *REST* nos fornece as ferramentas para lidar com isso, através de um **decorator** chamado **api_view**. 

**Já adianto que esse método será substituído posteriormente pelos Class Based View e posteriormente por Classes Genéricas.**

Iremos usar ele nas nossas funções e dizer quais *métodos* elas aceitam. Dessa maneira, o próprio Rest Framework passará a interpretar essas *views* como views de uma API que retorna objeto json, portanto, mesmo que um erro aconteça, ele retornará um json com o erro *404 Not Found*. Nesse primeiro caso, colocamos que o método aceito é somente o **GET**, portanto se tentarmos utilizar o método **DELETE**, por exemplo, dará um erro **405 Method Not Allowed**, e retornará um objeto json com o erro.

# Criando um agendamento<h2>
Para criar um agendamento iremos utilizar a mesma view (mesma url) de *agendamento_list*, porém o método, ao invés de *GET*, será o *POST* (lembre-se de incluir o 'POST' na api_view). Para isso fazemos algumas alterações no código, dizendo que se o método for *GET* mantemos aquele código que tínhamos, mas se o método for o *POST* teremos um código um pouco diferente. Como estamos utilizando a *api_view*, que é específica da Rest, não precisamos utilizar o *request.POST.data...*, agora podemos simplesmente pegar nossos dados com *request.data*. 

Como estamos utilizando o serializer, através do *AgendamentoSerializer* e passando o **data=data**, ele já ia validar nossas informações através do **serializer.is_valid()**, que quando validado, ele é populado automaticamente. Agora temos um dicionário com os dados válidos e iremos criar um objeto com esses valores. Retornamos então uma resposta **Status 201 Created**. Caso o *serializer.is_valid* não for valido, ou seja, os dados passados não são válidos, nós retornamos um *JsonResponse* com um **serializer.errors** com o **Status 400 Bad Request**.

# Editando um agendamento<h2>
Iremos implementar dois métodos, o *PUT* e o *PATCH*. Eles vão na mesma rota o *agendamento_detail*, ou seja, é necessário passar o *id* do agendamento de interesse. Mesmo esquema de passar os métodos na api_view e o *if request method*. Agora vamos a implementação do *PUT*. Queremos alterar os atributos que vieram em nossa requisição *request.data*. Do mesmo jeito que precisamos validar os atributos para criar um objeto, nós precisamos validar os atributos que estão sendo alterados na nossa requisição, portanto fazemos o mesmo esquema feito acima para criar um agendamento válido. Este método será substituído quando usarmos *Class Based Views* e não ficará tão repetitivo. Se tudo der certo iremos retornar um *JsonResponse* com os *dados atualizados* e o **Status 200 OK**. Lembrando que para o método *PUT* é necessário passar **todos** os atributos (Update Total), o que também é chamado de *Substituir uma Entidade*, diferentemente do *PATCH* (Update Parcial).

# Editando Parcialmente um agendamento<h2>
Iremos implementar o método *PATCH* em nosso projeto, visto que ele é melhor para nosso projeto, uma vez que podemos alterar **parcialmente** nosso objeto, e se quisermos alterar ele todo é só passar todos os atributos. Então iremos alterar o método *PUT*. Se só alterarmos o *PUT* para *PATCH*, ainda será necessário passar todos os campos, pois para validar ele está olhando o arquivo *AgendamentoSerializer*, então iremos alterar no *serializer.py* os atributos para **required=False**. Dessa maneira podemos alterar somente o atributo de nosso interesse. Porém se fizermos isso, sempre que for utilizar o *AgendamentoSerializer*, não será necessário passar todos os atributos, portanto, se quisermos criar um agendamento sem o nome do cliente, não irá encontrar o campo *nome_cliente* no *validated.data*, o que irá gerar um erro **Status 500 Internal Server Error**. Precisamos utilizar o mesmo serializer em dois lugares diferentes (Regras de Negócios Diferentes), em um sendo **obrigatório** passar todos os dados e em outro não. Então ao invés de alterar no *serializer.py*, colocamos um **partial=True** na nossa *view* do *PATCH*. Porém, o *serializer.data* ainda irá procurar todos os campos no *JsonResponse*, e para corrigir isso, passamos *validated_data* dentro do nosso *JsonResponse*. Dessa maneira, quando fizermos a requisição através do *Postman*, será retornado somente o atributo alterado.

**Observação:** um campo ser ou não *required* é diferente do campo ser ou não *válido*, ou seja, posso não precisar passar determinado campo, mas se eu passei, ele tem que ser válido perante nossas **Regras de Negócios**.

# Cancelando um agendamento<h2>
Agora iremos implementar a rota *DELETE*, que é a rota de **deletar** um objeto, porém depois iremos alterá-la para que ao invés de deletar, nós possamos **cancelar** este objeto.

Para isso usaremos a rota do *agendamento_detail*, visto que é necessário passar um *id* para deletar. Para isso inserimos o método *DELETE* em nossa *api_view*. Mais uma vez, buscamos o nosso objeto através do *get_object_or_404*, e usamos o método *obj.delete()* que tem em toda instância de modelo no Django. Depois disso retornamos uma *Response* (importada do rest_framework.response) vazia e um **Status Code 204 No Content**.

Porém, como falado anteriormente, para *Regra de Negócio* seria mais interessante *Cancelar* ao invés de *Deletar*, portanto, iremos fazer algumas alterações no nosso código para que isso seja implementado. Inserimos no nosso *models.py* o atributo **horario_cancelado** como um tipo *booleano*, que por padrão está definido como *default=False*, e no nosso método *DELETE*, quando fazemos essa requisição, altera de *False* para *True*. Depois de adicionar esse atributo ao nosso modelo, devemos fazer a **migração**, como visto anteriormente.

Mais uma coisa, de acordo com nossa *Regra de Negócios*, nós **não** queremos listar os **horários cancelados**, portanto iremos fazer um *queryset = Agendamento.objects.exclude(horario_cancelado=True)*.

# Refatorando nossa API<h2>
Agora iremos refatorar nossa aplicação, ou seja, não iremos mudar o comportamento dela, mas iremos melhorar como o código está apresentado, seja através de melhor *legibilidade, performance, arquitetura*. Nesse caso iremos focar na **legibilidade e manutenção**, ou seja, iremos refatorar para que tenha  menos código para ser gerido e mudado ao longo do tempo.

Para isso iremos começar alterando nosso *Serializer*. Iremos criar dois métodos que existem na *classe base serializer*, e vamos sobrescrever esses métodos. O primeiro é o método **create**, que quando começamos a escrever a função, o próprio VSCode já sugere sua implementação padrão, utilizando o **super** para chamar da *classe mãe*. Porém nesse caso, não é isso que queremos, iremos definir como um objeto *agendamento* é criado a partir de nosso serializer, ou seja, nosso serializer estará responsável tanto pela lógica de **validação dos dados**, quanto de **criação** dos *validated_data* que vem do *request*. E para isso iremos recortar o *código de criação* que está em nossa *view* e retornaremos uma instância. E na nossa *view*, ao invés de chamarmos *validated_data=serializer.validated_data* só usamos o **serializer.save()**. Como estamos usando uma *FrameWork*, ela tem vários métodos e ordem de chamada de métodos, e uma das coisas que o *RestFramework* faz quando chama o método *save* é que ele vai chamar o método *create* em algum momento do fluxo dele para criar um nova instância daquela classe. Então o método *create* não está sendo chamado diretamente pela gente, mas é chamado em algum momento na classe serializer quando chamamos o *save*. Portanto nossa *view* ficou muito mais limpar, nós basicamente tem que cuidar da parte de buscar os dados através do *request*, criar uma instância através do *AgendamentoSerializer* e então salvar esse serializer.

Além de usar o serializer para *criar* um objeto, também podemos usar ele para *atualizar* um objeto sobrescrevendo o método **update**. Mesmo esquema, se começarmos a digitar já aparece a sugestão de implementação igual o *create*, porém no *update* pede a *instância*. Lembrando, quando vamos atualizar um objeto no banco de dados, ele busca aquela *instância (objeto)* no banco de dados, pega os *dados da requisição* que passamos (validated_data), e depois **substitui esses dados na instância**. Então recortamos todo o código da nossa *view* e colamos na função *update*, lembrando de trocar o **obj** por **instance**. Depois é só retornar nossa *instância atualizada*. Depois chamamos na nossa *view* o *serializer.save()*. Observe que nos dois casos chamamos o *serializer.save*, e fica a dúvida, como ia saber se era pra chamar o *create* ou o *update*, mas no *RestFramework* ele tem um método para saber qual chamar. Se você passar somente o *validated_date* na requisição, ele entende que é pra *criar*, mas se chamar uma *instance*, ele entende que é para fazer o *update*.