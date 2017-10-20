from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

ButtonPressed = 0

@app.route('/button', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        global ButtonPressed
        ButtonPressed = ButtonPressed + 1
    return render_template("button.html", ButtonPressed = ButtonPressed)

if __name__ == '__main__':
    app.run()
