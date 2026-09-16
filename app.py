from flask import Flask
app = Flask(__name__)

# ========== HOME PAGE ==========
@app.route("/")
def home():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
      * { font-family: 'Chakra Petch', sans-serif; }
      body { background-color: #f0f4ff; }
    </style>

    <div class="container py-4">
      <h1 class="text-center text-primary display-4">Understanding Programming in Simple Words</h1>
      <hr class="my-4">

      <div class="card p-4 shadow-sm mb-4">
        <p class="lead">I am a beginner programmer studying to become a Backend Developer. Through this website, I explain basic programming concepts in simple language!</p>
        <p>Many people think programming requires advanced math or being a genius — but it's actually about logic, practice, and patience! Anyone can learn!</p>
      </div>

      <h4 class="text-dark mb-3">📚 Concepts:</h4>
      <ul class="list-group mb-4">
        <li class="list-group-item"><a href="/programming-logic" class="text-decoration-none">🧠 Programming Logic</a></li>
        <li class="list-group-item"><a href="/variables" class="text-decoration-none">📦 Variables</a></li>
        <li class="list-group-item"><a href="/functions" class="text-decoration-none">⚙️ Functions</a></li>
        <li class="list-group-item"><a href="/oop" class="text-decoration-none">🧍 OOP — Object-Oriented Programming</a></li>
        <li class="list-group-item"><a href="/database" class="text-decoration-none">💾 Database</a></li>
        <li class="list-group-item"><a href="/framework" class="text-decoration-none">🛠️ Framework</a></li>
      </ul>
    </div>
    """

# ========== PROGRAMMING LOGIC ==========
@app.route("/programming-logic")
def programming_logic():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
      * { font-family: 'Chakra Petch', sans-serif; }
      body { background-color: #f0f4ff; }
    </style>

    <div class="container py-4">
      <h1 class="text-center text-primary display-4">Programming Logic</h1>
      <hr class="my-4">
      <div class="card p-4 shadow-sm mb-4">
        <p class="lead">Logic is the way we think and organize steps to solve a problem. It's like giving very clear instructions to a computer!</p>
        <p>Just like following a recipe step-by-step: you tell the computer WHAT to do, IN WHICH ORDER, and UNDER WHICH CONDITIONS.</p>
      </div>
      <h5>Example:</h5>
      <pre class="bg-light p-3 rounded border">
if age >= 18:
    print("You are an adult!")
else:
    print("You are underage!")
      </pre>
      <br>
      <a href="/" class="btn btn-primary">Go Back</a>
    </div>
    """

# ========== VARIABLES ==========
@app.route("/variables")
def variables():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
      * { font-family: 'Chakra Petch', sans-serif; }
      body { background-color: #f0f4ff; }
    </style>

    <div class="container py-4">
      <h1 class="text-center text-primary display-4">Variables</h1>
      <hr class="my-4">
      <div class="card p-4 shadow-sm mb-4">
        <p class="lead">A variable is like a BOX where you store information! It can hold names, numbers, text — anything!</p>
        <p>You give it a name, put something inside, and use that name whenever you need the information later.</p>
      </div>
      <h5>Example:</h5>
      <pre class="bg-light p-3 rounded border">
name = "Alice"
age = 17
height = 1.65
print(f"My name is {name}, I'm {age} years old!")
      </pre>
      <br>
      <a href="/" class="btn btn-primary">Go Back</a>
    </div>
    """

# ========== FUNCTIONS ==========
@app.route("/functions")
def functions():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
      * { font-family: 'Chakra Petch', sans-serif; }
      body { background-color: #f0f4ff; }
    </style>

    <div class="container py-4">
      <h1 class="text-center text-primary display-4">Functions</h1>
      <hr class="my-4">
      <div class="card p-4 shadow-sm mb-4">
        <p class="lead">A Function is a block of code that does ONE specific job. You write it ONCE and use it MANY times!</p>
        <p>Think of it like a machine: you put something IN, it does the work, and gives you something BACK.</p>
      </div>
      <h5>Example:</h5>
      <pre class="bg-light p-3 rounded border">
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
      </pre>
      <br>
      <a href="/" class="btn btn-primary">Go Back</a>
    </div>
    """

# ========== OOP ==========
@app.route("/oop")
def oop():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
      * { font-family: 'Chakra Petch', sans-serif; }
      body { background-color: #f0f4ff; }
    </style>

    <div class="container py-4">
      <h1 class="text-center text-primary display-4">OOP — Object-Oriented Programming</h1>
      <hr class="my-4">
      <div class="card p-4 shadow-sm mb-4">
        <p class="lead">OOP organizes code into "Objects" that represent real things! Like a blueprint to create houses!</p>
        <p>A <strong>Class</strong> is the blueprint. An <strong>Object</strong> is the actual house built from that blueprint.</p>
      </div>
      <h5>Example:</h5>
      <pre class="bg-light p-3 rounded border">
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

me = Person("Alice", 17)
print(f"My name is {me.name}")
      </pre>
      <br>
      <a href="/" class="btn btn-primary">Go Back</a>
    </div>
    """

# ========== DATABASE ==========
@app.route("/database")
def database():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
      * { font-family: 'Chakra Petch', sans-serif; }
      body { background-color: #f0f4ff; }
    </style>

    <div class="container py-4">
      <h1 class="text-center text-primary display-4">Database</h1>
      <hr class="my-4">
      <div class="card p-4 shadow-sm mb-4">
        <p class="lead">A Database is an organized place to store information permanently. Like a digital filing cabinet!</p>
        <p>Databases let you: <strong>Create</strong> → <strong>Read</strong> → <strong>Update</strong> → <strong>Delete</strong> information easily.</p>
      </div>
      <h5>Example (SQL):</h5>
      <pre class="bg-light p-3 rounded border">
CREATE TABLE users (
    name TEXT,
    age INTEGER
);

INSERT INTO users VALUES ("Alice", 17);
SELECT * FROM users;
      </pre>
      <br>
      <a href="/" class="btn btn-primary">Go Back</a>
    </div>
    """

# ========== FRAMEWORK ==========
@app.route("/framework")
def framework():
    return """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
      * { font-family: 'Chakra Petch', sans-serif; }
      body { background-color: #f0f4ff; }
    </style>

    <div class="container py-4">
      <h1 class="text-center text-primary display-4">Framework</h1>
      <hr class="my-4">
      <div class="card p-4 shadow-sm mb-4">
        <p class="lead">A Framework is a set of ready-made tools that help you build things faster! It gives you a solid foundation so you don't have to start from zero!</p>
        <p><strong>Flask</strong> is a Python framework specifically made for creating websites easily!</p>
      </div>
      <h5>Example — This very website:</h5>
      <pre class="bg-light p-3 rounded border">
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
      </pre>
      <br>
      <a href="/" class="btn btn-primary">Go Back</a>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)
