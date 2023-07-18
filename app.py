from flask import Flask, render_template, request, redirect,  make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Integer, Sequence
import os


abs_instance_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'instance')) #<--- this will be the instance directory
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(15), nullable=False)
    more_info = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

 
    def _repr_(self) -> str:
        return f"{self.sno}-{self.title}"

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST':
        return redirect("/home")
    if request.method=='POST':
        return redirect("/support")
    return render_template('index.html')


@app.route('/home', methods= ['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title=request.form['title']
        desc=request.form['desc']
        more_info=request.form['more_info']
        todo= Todo(title=title, desc=desc, more_info=more_info) 
        db.session.add(todo)
        db.session.commit()
    allTodo=Todo.query.all()
    return render_template ('home.html', allTodo=allTodo) 


@app.route('/show')
def products():
    allTodo=Todo.query.all()
    print(allTodo)
    return 'This is product page.'


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        more_info= request.form['more_info']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        todo.more_info= more_info
        db.session.add(todo)
        db.session.commit()
        return redirect("/home")
        
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/home")

@app.route('/support/', methods=['GET','POST'])
def support():
    return render_template('support.html')

@app.route('/', methods=['GET','POST'])
def get_started():
    return redirect('/home')

if __name__ == "__main__":
    app.run(debug=True, port=8000)