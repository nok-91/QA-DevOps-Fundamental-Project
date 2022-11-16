from application import app, db
from application.models import Category, Task
from application.forms import AddCategory, AddTask, UpdateTask
from flask import render_template, redirect, url_for, request
from sqlalchemy import asc

@app.route('/')
def home():
    data = db.session.query(Task, Category).join(Category).all()
    print(data)
    return render_template('home.html', data=data)
        


@app.route('/add-category', methods=['GET','POST'])
def add_category():
    form = AddCategory()
    if request.method == 'POST':
        if form.validate_on_submit():
            cat_title = form.category_title.data
            newcategory = Category(category_title = cat_title)
            db.session.add(newcategory)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_category.html', form=form)




@app.route('/add-task', methods=['GET','POST'])
def add_task():
    form = AddTask()
    categories = Category.query.all()
    for category in categories:
        form.category.choices.append((category.category_id, category.category_title))
    if request.method == 'POST':
        if form.validate_on_submit():
            t_description = form.description.data
            t_date = form.date.data
            t_cat = form.category.data
            newtask = Task(description = t_description, date = t_date, category_id = t_cat)
            db.session.add(newtask)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_task.html', form=form)



@app.route('/update-task/<int:tid>', methods=['GET','POST'])
def update_task(tid):
    form = UpdateTask()
    if request.method == 'POST':
        t_description = form.description.data
        t_date = form.date.data
        t_completed = Task.completed
        task = Task.query.filter_by(task_id=tid).first()
        task.description = t_description
        task.date = t_date
        task.completed = t_completed
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update_task.html', form=form)



@app.route('/delete-task/<int:tid>')
def delete_task(tid):
    task = Task.query.filter_by(task_id=tid).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))



@app.route('/is-complete/<int:tid>')
def is_complete(tid):
        iscomp = Task.query.filter_by(task_id=tid).first()
        if iscomp.completed == False:
            iscomp.completed = True
        else:
            iscomp.completed = False
        db.session.commit()
        return redirect(url_for('home'))
  



