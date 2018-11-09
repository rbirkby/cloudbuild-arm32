from flask import Flask
import os

port = int(os.environ.get("PORT", 8080))

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
    