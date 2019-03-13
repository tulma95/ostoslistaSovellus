import flask from Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return  "hei maailma"


if __name__ == "__MAIN__":
    app.run()