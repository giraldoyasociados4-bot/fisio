from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema web funcionando en la nube"

if __name__ == "__main__":
    app.run()