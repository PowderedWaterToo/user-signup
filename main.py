from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/welcome", methods=['POST'])
def welcome_user():
    # look inside the request to figure out what the user typed
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']

    uerror = ""
    perror = ""
    verror = ""

    # if the user typed nothing at all, redirect and tell them the error
    if (not username) or (username.strip() == ""):
        uerror = "You must type a valid username."

    if (not password) or (password.strip() == ""):
        perror = "You must enter a password."

    if (not vpassword) or (vpassword.strip() == ""):
        verror = "You must verify your password."

    if len(email) == 0:
        eerror = ""
    elif "@" not in email or "." not in email or len(email)<3 or len(email)>20 or " " in email:
        eerror = "You must enter a valid email address between 3 and 20 characters with no spaces."

    if len(uerror)>0 or len(perror)>0 or len(verror)>0 or len(eerror)>0:
        return redirect("/?uerror=" + uerror + "&perror=" + perror + "&verror=" + verror + "&eerror=" + eerror)


    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    username_escaped = cgi.escape(username, quote=True)

    # TODO:
    # Create a template called add-confirmation.html inside your /templates directory
    # Use that template to render the confirmation message instead of this temporary message below
    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    encoded_uerror = request.args.get("uerror")
    encoded_perror = request.args.get("perror")
    encoded_verror = request.args.get("verror")
    encoded_eerror = request.args.get("eerror")

    return render_template('home.html', uerror=encoded_uerror and cgi.escape(encoded_uerror, quote=True), perror=encoded_perror and cgi.escape(encoded_perror, quote=True), verror=encoded_verror and cgi.escape(encoded_verror, quote=True), eerror=encoded_eerror and cgi.escape(encoded_eerror, quote=True))


app.run()