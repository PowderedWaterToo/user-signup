from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/welcome", methods=['POST'])
def welcome_user():
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']

    uerror = ""
    perror = ""
    verror = "" 
    eerror = ""

    if (not username) or (username.strip() == "") or " " in username or len(username)<3 or len(username)>20:
        uerror = "You must type a valid username with no spaces between 3 and 20 characters."

    if (not password) or (password.strip() == "") or " " in password or len(password)<3 or len(password)>20:
        perror = "You must type a valid password with no spaces between 3 and 20 characters."

    if vpassword != password:
        verror = "The password you entered does not match the Password above."

    if len(email) == 0:
        eerror = ""
    elif "@" not in email or "." not in email or len(email)<3 or len(email)>20 or " " in email:
        eerror = "You must enter a valid email address between 3 and 20 characters with no spaces."

    if len(uerror)>0 or len(perror)>0 or len(verror)>0 or len(eerror)>0:
        return redirect("/?uerror=" + uerror + "&perror=" + perror + "&verror=" + verror + "&eerror=" + eerror + "&email=" + email + "&username=" + username)

    username_escaped = cgi.escape(username, quote=True)

    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    encoded_uerror = request.args.get("uerror")
    encoded_perror = request.args.get("perror")
    encoded_verror = request.args.get("verror")
    encoded_eerror = request.args.get("eerror")
    email = request.args.get("email")
    username = request.args.get("username")

    return render_template('home.html', uerror=encoded_uerror and cgi.escape(encoded_uerror, quote=True), perror=encoded_perror and cgi.escape(encoded_perror, quote=True), verror=encoded_verror and cgi.escape(encoded_verror, quote=True), eerror=encoded_eerror and cgi.escape(encoded_eerror, quote=True), email=email and cgi.escape(email, quote=True), username=username and cgi.escape(username, quote=True))


app.run()