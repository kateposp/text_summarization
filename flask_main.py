import sys
import typing as tp

import flask
from flask import render_template, request
from flask_cors import CORS

from text_manager import TextManager


PORT: int = 5000
BASE_URL: str = "http://localhost:"

app = flask.Flask(__name__,
                  static_url_path='',
                  static_folder='web/static',
                  template_folder='web/templates')
CORS(app)

text_manager: tp.Optional[TextManager] = TextManager()


@app.route('/')
def home():
    return render_template("front.html")


@app.route('/summarize', methods=['POST'])
def login():
    print("I am exist", file=sys.stderr)
    if request.method == "POST":
        data = request.get_json(force=True)
        text_manager.set_text(data["text"])

        result = {
            "text": text_manager.get_summarized_text()
        }
        return result, 200


if __name__ == '__main__':
    app.run(port=PORT, debug=True)
