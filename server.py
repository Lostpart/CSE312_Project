import sys

from flask import Flask

app = Flask(__name__, static_url_path='')


@app.route("/")
def index():
    return app.send_static_file("index.html")


if __name__ == '__main__':
    port = 8080
    if len(sys.argv) >= 2:
        port = sys.argv[1]
    app.run(host="0.0.0.0", port=port, debug=True)
