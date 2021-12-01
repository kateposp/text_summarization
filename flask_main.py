import flask
from flask import render_template, request

from text_manager import TextManager

PORT: int = 5000
BASE_URL: str = "http://localhost:"

app = flask.Flask(__name__,
                  static_folder='web/static',
                  template_folder='web/templates')

text_manager: TextManager = TextManager()


@app.route('/')
def home():
    return render_template("front.html")


@app.route('/summarize', methods=['POST'])
def login():
    data = request.get_json()
    text_manager.set_text(data["text"])
    result = {
        "text": text_manager.get_summarized_text()
    }
    return result, 200


if __name__ == '__main__':
    app.run(port=PORT, debug=True)
