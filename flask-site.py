from flask import Flask, render_template, url_for

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "sebayeva"

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
    }
]
@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', people=people)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)