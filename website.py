from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    
    instagram = url_for('static', filename='instagram.png')
    email = url_for('static', filename='email.png')
    linkedin = url_for('static', filename='linkedin.png')
    github = url_for('static', filename='github.png')

    
    return render_template("index.html",instagram=instagram,email=email,linkedin=linkedin,github=github)


@app.route("/about")
def about():

    image_file = url_for('static', filename='myPic.png')
    return render_template('about.html', image_file=image_file)
   


@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)
