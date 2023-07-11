from flask import Flask, render_template, request, session, redirect, flash


app = Flask(__name__)
app.secret_key = 'super-secret-key'


# -----------------------------Home Page---------------------------
@app.route('/')
def home():
    return render_template('index.html')

# -------------------------Courses Page---------------------------


@app.route('/course')
def course():
    return render_template('course.html')

# -------------------------About Page-----------------------------------


@app.route('/about')
def about():
    return render_template('about.html')

# -------------------------Contact Page-----------------------------------


@app.route('/contact')
def contact():
    return render_template('contact.html')

# -------------------------Blog Page-----------------------------------


@app.route('/blog')
def blog():
    return render_template('blog.html')

# --------------------------login Page and Dashboard Page---------------------------------------


@app.route('/login', methods=['GET', 'POST'])
def login():
    if ('user' in session and session['user'] == "Voldemort"):
        return render_template('dashboard.html')

    if (request.method == "POST"):
        username=request.form.get('uname')
        userpass=request.form.get('password')
        if (username == "Voldemort" and userpass == "tombriddle123"):
            # set the session variable
            session['user']=username
            return render_template('dashboard.html')
        else:
            flash('Wrong Id or Password')

    return render_template('login.html')



@ app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
