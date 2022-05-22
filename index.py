
from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask("__name__")
run_with_ngrok(app)

@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/camera.html")
def camera():
    return render_template("camera.html")


@app.route("/location.html")
def location():
    return render_template("location.html")





if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run()

