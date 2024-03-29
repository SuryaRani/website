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
    first_project = url_for('static', filename='websitePic.png')
    second_project = url_for('static', filename='simpleServerPic.png')
    third_project = url_for('static', filename='multithreadingPic.png')
    fourth_project = url_for('static', filename='loadBalancer.png')
    fifth_project = url_for('static', filename='cachePic.png')
    return render_template("projects.html",first_project=first_project,second_project=second_project,third_project=third_project,fourth_project=fourth_project,fifth_project=fifth_project)

if __name__ == "__main__":
    app.run(debug=True)
