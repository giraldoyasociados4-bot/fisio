from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "que guapo morro"

if __name__ == "__main__":
    app.run()