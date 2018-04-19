from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

counts = 0

@app.route("/")
def index_page():
    return redirect("/frontend")

@app.route("/frontend")
def frontend_page():
    return render_template("frontend.html")

@app.route("/request_counter")
def request_counter():
    global.counts



if __name__ == "__main__":
    app.run(
        debug = True,
        port = 5000
    )