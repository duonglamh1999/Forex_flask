from asyncio.windows_events import NULL
from flask import Flask, redirect, request, render_template,session,flash
from flask_debugtoolbar import DebugToolbarExtension
from converter import convert,check
app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

RESPONSES_KEY = "responses"

@app.route("/")
def start():
    value=None
    return render_template('form.html')

@app.route("/convert",methods=["POST"])
def handle_response():
    cur1 = request.form.get("Current1")
    cur2 = request.form.get("Current2")
    amount = request.form.get("Amount")
    checking = check([cur1,cur2],amount)
    if len(checking)>0:
        for message in checking:
            flash(message)
        return redirect('/')
    global value
    value=convert(cur1,cur2,amount)
    return redirect('/answer')

@app.route("/answer")
def answer():
    return render_template('answer.html',value= value)