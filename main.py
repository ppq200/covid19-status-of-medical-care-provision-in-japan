from flask import Flask
from src.task import main

app = Flask(__name__)


@app.route("/health")
def health():
    return "health is ok"


@app.route("/do", methods=["POST"])
def do():
    message = main()
    app.logger.info(message)
    return message


if __name__ == "__main__":
    main()
