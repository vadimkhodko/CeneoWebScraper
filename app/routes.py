from app import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello World"

@app.route("/name",defaults={'name' :"Anonim"})
@app.route("/name/<name>")
def name(name):
    return f"Hello {name}"