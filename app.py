from flask import Flask, render_template, request, redirect, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.now)
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

with app.app_context():
    # within this block, current_app points to app.
    print(current_app.name)
    db.create_all()

@app.get('/')
def home_html():
    return render_template("homepage.html")

@app.get('/homepage.html')
def homepage_html():
    return render_template("homepage.html")

@app.get('/login.html')
def login_html():
    return render_template("login.html")

@app.get('/about.html')
def about_html():
    return render_template("about.html")

@app.get('/local_login.html')
def local_login_html():
    return render_template("local_login.html")
    
@app.get('/local_home_page.html')
def local_homepage_html():
    return render_template("local_home_page.html")

@app.get('/local_guide_page.html')
def local_guidepage_html():
    return render_template("local_guide_page.html")

@app.get('/local_food_rec.html')
def local_food_rec_html():
    return render_template("local_food_rec.html")

@app.get('/local_place_rec.html')
def local_place_rec_html():
    return render_template("local_place_rec.html")

@app.get('/emergency_nos.html')
def emergency_nos_html():
    return render_template("emergency_nos.html")

@app.get('/language_course.html')
def language_course_html():
    return render_template("language_course.html")

@app.get('/login2.html')
def login2_html():
    return render_template("login2.html")

@app.get('/Delhi.html')
def Delhi_html():
    return render_template("Delhi.html")

@app.route('/todo.html', methods=['GET', 'POST'])
def todo_html():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template("todo.html", allTodo=allTodo)

# @app.route('/show')
# def show_todo():
#     allTodo = Todo.query.all()
#     print(allTodo)
#     return "Hello World"

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update_todo(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/todo.html')
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todo=todo)

@app.route('/delete/<int:sno>')
def delete_todo(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/todo.html')

if __name__ == "__main__":
    app.run(debug=True)