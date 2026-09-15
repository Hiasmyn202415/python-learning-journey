from flask import Flask
app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <div class="container py-4">

    <h1 class="text-center text-primary display-4">Explicando a programação de maneira simples</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Sou uma iniciante em programação, estou estudando para me tornar uma dev em backend, através deste site vim explicar alguns conceitos básicos e esclarecer algumas coisas e dúvidas frequentes...vamos lá?</p>
    <p>As pessoas costumam acreditar que a programação envolve inglês e matemática, porém é aí onde se enganam...não vou dizer que não existe inglês na programação, pois as variáveis e comandos são escritos em inglês, entretanto não é nada assustador e difícil de se aprender e memorizar, referente a matemática...não é necessário ser bom em matemática. A programação envolve lógica e nosso objetivo é resolver problemas com essa lógica e comandos dependendo da linguagem, então sim é um mito ser necessário ter inglês e matemática para esse aprendizado.</p>
    </div>

    <h4 class="text-dark mb-3">Conceitos Básicos:</h4>
    <ul class="list-group mb-4">
    <li class="list-group-item"><a href="/logica" class="text-decoration-none">Lógica de Programação</a></li>
    <li class="list-group-item"><a href="/variaveis" class="text-decoration-none">Variáveis</a></li>
    <li class="list-group-item"><a href="/funcoes" class="text-decoration-none">Funções</a></li>
    <li class="list-group-item"><a href="/poo" class="text-decoration-none">POO</a></li>
    <li class="list-group-item"><a href="/bancodedados" class="text-decoration-none">Banco de dados</a></li>
    <li class="list-group-item"><a href="/framework" class="text-decoration-none">Framework</a></li>
    </ul>

    </div>
    """

@app.route("/logica")
def logica():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <div class="container p-4">

    <h1 class="text-center text-primary display-4">Lógica de programação</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">A lógica de programação é a técnica de organizar o pensamento em uma sequência clara, lógica e ordenada de passos para resolver um problema que o computador consegue executar.</p>
    </div>

    <h5>Exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
Inicio
    Escrever "Digite um número:"
    Ler numero
    Se numero % 2 == 0 então
        Escrever "O número é par"
    Senão
        Escrever "O número é ímpar"
Fim
    </pre>

    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>

    </div>
    """

@app.route("/variaveis")
def variaveis():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <div class="container p-4">

    <h1 class="text-center text-primary display-4">Variáveis</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Uma variável é uma característica ou atributo de interesse que pode ser medido ou coletado e cujos valores mudam de um elemento para outro em uma amostra.</p>
    </div>

    <h5>Por exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
nome = "Maria"
    </pre>

    <br>
    <a href="/" class="btn btn-primary">Volte a Página inicial</a>

    </div>
    """

@app.route("/funcoes")
def funcoes():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <div class="container py-4">

    <h1 class="text-center text-primary display-4">Funções</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Uma função na programação é um bloco de código reutilizável projetado para realizar uma tarefa específica.</p>
    </div>

    <h5>Por exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
def saudacao(nome):
    return f"Olá, {nome}!"
    </pre>

    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>

    </div>
    """

@app.route("/poo")
def poo():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <div class="container p-4">

    <h1 class="text-center text-primary display-4">POO</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">A Programação Orientada a Objetos (POO) em Python é um paradigma que organiza o código em torno de Classes, Objetos e Atributos para simular o mundo real.</p>
    </div>

    <h5>Por exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.modelo} está ligado.")

meu_carro = Carro("Toyota", "Corolla")
meu_carro.ligar()
    </pre>

    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>

    </div>
    """

@app.route("/bancodedados")
def bancodedados():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <div class="container p-4">

    <h1 class="text-center text-primary display-4">Banco de dados</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">O Python se conecta a bancos de dados de forma simples usando bibliotecas nativas como o sqlite3 ou ferramentas avançadas como o SQLAlchemy.</p>
    </div>

    <h5>Por exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
import sqlite3

conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Ana', 25)")
conexao.commit()

cursor.execute("SELECT * FROM usuarios")
for linha in cursor.fetchall():
    print(linha)

conexao.close()
    </pre>

    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>

    </div>
    """

@app.route("/framework")
def framework():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <div class="container p-4">

    <h1 class="text-center text-primary display-4">Framework</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Um framework na programação Python é uma base pronta com regras e ferramentas que ajuda a criar programas mais rápido.</p>
    </div>

    <h5>Por exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
1. Django (Desenvolvimento Web)
2. Flask (Desenvolvimento Web)
3. FastAPI (APIs e Web)
4. TensorFlow (Inteligência Artificial)
5. PyTorch (Inteligência Artificial)
    </pre>

    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>

    </div>
    """

@app.route("/funcoes")
def funcoes():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <div class="container py-4">

    <h1 class="text-center text-primary display-4">Funções</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Uma função na programação é um bloco de código reutilizável projetado para realizar uma tarefa específica.</p>
    </div>

    <h5>Por exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
def saudacao(nome):
    return f"Olá, {nome}!"
    </pre>

    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>

    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)
