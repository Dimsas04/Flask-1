from flask import *
from tasks import *
from datetime import *
import datetime
from AddTaskForm import AddTaskForm

app=Flask(__name__)
app.config['SECRET_KEY']='87c725f6be51b16e19446e14b59149e7'

tasks=[
    task("Get a Haircut",datetime.date(2024,2,20)),
    task("Buy Groceries",datetime.date(2024,1,19)),
    task("Attend Birthday",datetime.date(2024,1,18))
]

@app.route("/maint",methods=['GET','POST'])
def maint():
    return render_template("test.html",tasks=tasks)

@app.route("/AddTask",methods=['GET','POST'])
def AddTask():
    form=AddTaskForm()
    if form.validate_on_submit():
        print("wehYYFIJksdgflakujshd")
        n_task=form.TaskName.data
        n_deadline=form.TaskDeadline.data
        obj=task(n_task,n_deadline)
        tasks.append(obj)
        return redirect(url_for('maint'))
    return render_template("AddTask.html",form=form)


setattr(tasks[2],'status',"DONE")
if(__name__=='__main__'):
    app.run(debug=True)