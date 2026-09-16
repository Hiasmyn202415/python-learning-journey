from flask import Flask
app = Flask(__name__)

# ========== PÁGINA INICIAL ==========
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

    <!-- MENU DE NAVEGAÇÃO -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light rounded mb-4">
      <div class="container-fluid">
        <a class="nav-link d-inline me-3" href="/about">👤 About Me</a>
        <a class="nav-link d-inline" href="/projects">💻 My Projects</a>
      </div>
    </nav>

    <h1 class="text-center text-primary display-4">Understanding Programming in Simple Words</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">I am a beginner in programming, studying to become a Backend Developer. Through this website, I explain basic concepts and clarify common doubts... let's go!</p>
    <p>Many people believe programming requires advanced English and complex math. But that's NOT true! Programming is about LOGIC, just like following a recipe step-by-step.</p>
    <p>Anyone can learn! You just need patience, practice, and consistency. Here I share my learning journey from zero to backend!</p>
    </div>

    <div class="card p-4 shadow-sm mb-4">
    <h3 class="text-secondary">🔹 Variables</h3>
    <p>Think of a variable like a BOX where you store information. It can hold text, numbers, or anything!</p>
    <pre class="bg-light p-3 rounded">name = "Maria"
age = 17</pre>
    </div>

    <div class="card p-4 shadow-sm mb-4">
    <h3 class="text-secondary">🔹 Functions</h3>
    <p>A function is a block of code that does something specific. You create it once and use it many times!</p>
    <pre class="bg-light p-3 rounded">def greet():
    return "Hello, welcome!"</pre>
    </div>

    <div class="card p-4 shadow-sm mb-4">
    <h3 class="text-secondary">🔹 Conditionals (If / Else)</h3>
    <p>Your program makes decisions! IF something is true → do this. ELSE → do that.</p>
    <pre class="bg-light p-3 rounded">age = 17
if age >= 18:
    print("You are an adult!")
else:
    print("You are underage!")</pre>
    </div>

    <div class="card p-4 shadow-sm mb-4">
    <h3 class="text-secondary">🔹 Loops (For / While)</h3>
    <p>Repeat actions automatically! No need to write the same code 100 times!</p>
    <pre class="bg-light p-3 rounded">for number in [1, 2, 3, 4, 5]:
    print(number)</pre>
    </div>

    <div class="card p-4 shadow-sm mb-4">
    <h3 class="text-secondary">🔹 Object-Oriented Programming (OOP)</h3>
    <p>Think of a CLASS like a "blueprint" or "template". From one blueprint, you can create many objects!</p>
    <pre class="bg-light p-3 rounded">class Person:
    def __init__(self, name):
        self.name = name

me = Person("Hiasmyn")
print(me.name)</pre>
    </div>

    <div class="card p-4 shadow-sm mb-4">
    <h3 class="text-secondary">🔹 Databases (SQL)</h3>
    <p>Where you store data permanently! Like a giant organized notebook. We use SQL to ask questions and get information.</p>
    <pre class="bg-light p-3 rounded">SELECT * FROM users;</pre>
    </div>

    <hr class="my-4">
    <div class="text-center">
    <p class="text-muted">🚀 Created by Hiasmyn — Learning Backend Development, one step at a time!</p>
    </div>
    </div>
    """

# ========== PÁGINA SOBRE MIM ==========
@app.route("/about")
def about():
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
    <nav class="navbar navbar-expand-lg navbar-light bg-light rounded mb-4">
      <div class="container-fluid">
        <a class="nav-link d-inline me-3" href="/">🏠 Home</a>
        <a class="nav-link d-inline" href="/projects">💻 My Projects</a>
      </div>
    </nav>

    <h1 class="text-center text-primary display-4">About Me</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Hi! I'm Hiasmyn! 👋</p>
    <p>I'm 17 years old and I'm on a journey to become a Backend Developer! 💻</p>
    <p>I work, I train, and I study programming late at night because I love it and I know where I want to go! 🎯</p>
    <p>Currently learning: Python → Flask → SQL → more!</p>
    <p>Dream: Work in tech internationally! 🌎✈️</p>
    </div>

    <div class="text-center mt-4">
      <a href="/" class="btn btn-primary">← Back to Home</a>
    </div>
    </div>
    """

# ========== PÁGINA DE PROJETOS ==========
@app.route("/projects")
def projects():
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
    <nav class="navbar navbar-expand-lg navbar-light bg-light rounded mb-4">
      <div class="container-fluid">
        <a class="nav-link d-inline me-3" href="/">🏠 Home</a>
        <a class="nav-link d-inline" href="/about">👤 About Me</a>
      </div>
    </nav>

    <h1 class="text-center text-primary display-4">My Projects</h1>
    <hr class="my-4">

    <div class="card p-4 shadow-sm mb-4">
      <h5 class="card-title">🌐 #1: Learning Journey Website</h5>
      <p class="card-text">This very site! Built with Flask, explaining programming basics.</p>
      <span class="badge bg-primary">Flask</span>
      <span class="badge bg-success">Python</span>
      <span class="badge bg-info">HTML/CSS</span>
    </div>

    <div class="card p-4 shadow-sm mb-4">
      <h5 class="card-title">🚧 #2: Coming Soon...</h5>
      <p class="card-text">Next project in development! Ideas: to-do list, login system, calculator...</p>
      <span class="badge bg-warning text-dark">In Progress</span>
    </div>

    <div class="text-center mt-4">
      <a href="/" class="btn btn-primary">← Back to Home</a>
    </div>
    </div>
    """

if __name__ == "__main__":
    app.run()
