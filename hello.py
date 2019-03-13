from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return  "hei maailma miten menee"


if __name__ == "__main__":
    app.run()

