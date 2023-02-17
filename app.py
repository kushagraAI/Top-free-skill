from flask import Flask

app = Flask(__name__)


@app.route("/")
def Topfreeskill():
  return "<p>Welcome to Top free skill</p>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
