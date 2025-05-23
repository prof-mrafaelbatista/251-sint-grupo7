# 251-sint-grupo7

## 📱 - Seja bem-vindo ao *Python Helper*, um projeto que utiliza Python, HTML e Flask para formar uma ferramenta que auxilia estudantes de Python com seus estudos. 

Composição do grupo: Gabriel Gomes Fernandes (SINT - noite) e Letícia da Silva Soares (SINT - noite).


📌 - Sumário:
    I - Estrutura do site e conteúdo;
    II - Tecnologias utilizadas;
    III - Como foi feita a integração com a API do Gemini;
    IV - Como executar a aplicação Flask localmente;
    V - Principais partes do código Python.


I. A estrutura do site e o conteúdo de cada seção;
    O site é chamado “Python Helper” e é composto por três páginas principais: “Home”, “Sobre a equipe”, “Tire sua dúvida” e “Glossário de termos”. O “Home” é um introdutório ao conteúdo do site, abordando tópicos como estruturas de seleção, estruturas de repetição, vetores e matrizes, funções e procedimentos e tratamentos de exceção.

    O “Sobre a equipe” contém informações sobre cada membro da equipe, como redes sociais e nome. O “Tire sua dúvida” contém uma integração com a API do Gemini que permite ao usuário fazer perguntas acerca do assunto.
    
    O “Glossário de termos” funciona como um dicionário com termos correlatos e possui suas próprias funcionalidades, como editar um termo, adicionar um termo e apagar um termo.


II. As tecnologias (linguagem de programação, bibliotecas, ...) utilizadas;
    Para o desenvolvimento do projeto, foi utilizada a pseudo linguagem “HTML”, para inserção de conteúdo visível no site, e a linguagem de programação “Python”, para garantir a funcionalidade do site. 
    
    Além disso, a biblioteca “Flask”, um micro-framework que facilita a integração do Python em aplicações web, a linguagem de marcação de texto “Markdown”, usada para formatar a resposta do Gemini, e a API do Gemini, a inteligência artificial da Google. 


III. Como a integração com a API do Gemini foi implementada;
    Ao acessar o Google AI for Developers, com uma conta Google, é possível gerar uma chave individual de API e é disponibilizado um código para a integração correta no projeto. É necessário instalar, em seu ambiente virtual, o “google-generativeai”, por intermédio do comando “pip install”, antes de tentar rodar o projeto. 

```Terminal
pip install google-generativeai
```
    
    No início do arquivo “app.py”, foi importado o “google.generativeai” com o nome de “gemini” para ser usado no código. Utilizando o “@app.route” e nomeando a função e métodos a serem usados, criou-se a função “duvidas”, que contém uma estrutura de seleção para buscar o que o usuário digitou na aba “Tire sua dúvida” e retorna uma resposta coerente com o prompt. 
    
    Na página “duvidas.html”, foi utilizado o símbolo de chaves e porcentagem para indicar o início e o fim do uso de uma função ou recurso Python. Nesse caso, para exibir a resposta, uma variável no arquivo Python, foram usadas as chaves e o nome da variável, além do “| safe” para formatar a resposta – dessa parte vem o uso do “Markdown”. 

```HTML e python
{% if resposta %}
<h2>Resposta:</h2>
<p>{{ resposta|safe }}</p> 
{% endif %}
```


IV. Como executar a aplicação Flask localmente;
    Em primeira instância, deve-se clonar os arquivos numa pasta local. Então, criar um ambiente virtual e dentro dele instalar a biblioteca Flask, a API do Gemini e o Markdown (opcional). Logo, basta rodar o arquivo “app.py” e acessar o link. 


V. Uma breve descrição das principais partes do código Python;
    No início, são feitas as importações e a configuração do Flask. Por conseguinte, são introduzidos os “@app.route”, cada um com uma função. Algumas são funções de redirecionamento das páginas HTML, uma vez que a inserção da tag “<a>” no HTML não é suficiente quando estamos utilizando um framework como o Flask. 
    
```python
@app.route('/')
def index():
return render_template('index.html')
# Exemplo de redirecionamento usando Flask
```

    Em outros, são funções específicas para cada página. Por exemplo, para a página de dúvidas, é definida uma função para que o Gemini fosse utilizável, o configurando corretamente. Para o glossário/dicionário, foram definidas funções para apagar um termo, adicionar um termo e alterar um termo.

