from controller import app

@app.route("/")
def index():
    return "Hello World Test2"