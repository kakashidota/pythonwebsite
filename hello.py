from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hej välkommen till min coola hemsida, <h1>detta är produktion.<h1>"

app.run()

