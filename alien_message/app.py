from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, json

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return redirect("/welcome", code = 302)

@app.route('/welcome')
def welcome():
    return render_template("index.html")

#route for challenge page        
@app.route('/decoding-message', methods=['POST','GET'])
def decode_message():
    if request.method == "POST":
        alien_massage = request.form.get("alien_massage").lower()
  
        if alien_massage == "send our troops on earth":
            return render_template("flag.html", title = "Flag")

        else:
            return render_template("attack.html", title = "They are here.")

    else:
        return redirect("/welcome", code = 302)

#route for flag
@app.route('/hint')
def nothing_hint():
    return render_template("hint.html", title = "Nothing Hint")

#for 404 error
@app.errorhandler(404)
def error_404(e):
    return render_template("404.html", title = "404 Error")

if __name__ == '__main__':
   app.run()

