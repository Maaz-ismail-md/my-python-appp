from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def P3():
    return render_template("P3.html")

@app.route("/P2")
def P2():
    return render_template("P2.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
