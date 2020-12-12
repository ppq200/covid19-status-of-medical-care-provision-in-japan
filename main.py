from flask import Flask
from src.task import main

app = Flask(__name__)


@app.route("/health")
def health():
    print("ok", flush=True)
    return "ok"


@app.route("/do", methods=["POST"])
def do():
    main()
    return "ok"


if __name__ == "__main__":
    main()
