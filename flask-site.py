from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "3e63407c98351c6073f49fc8976ee533"

    return app

app = create_app()


people = [
    {
    'name': "Sebastian",
    'age' : 18,
    'job' : "Jobless"
    }, 
    {
    'name': "Eva",
    'age' : 16,
    'job' : "Sushi Bar"
    },
    {
    'name': "Jose Luis Torresola",
    'age': "???",
    'job': "retired"
    }    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', people=people)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():   
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login")
def login():   
    form = LoginForm()
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)