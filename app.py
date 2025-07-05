from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ["Pick kids from school", "Take the dog for a walk", "Take the car for a MOT"]

@app.route("/")
@app.route("/index")
def index():
  return render_template("index.html")

@app.route("/task")
def task_list():
  return render_template("tasks.html", tasks=tasks)

@app.route("/addtask", methods=["GET"])
def add_task_get():
  return render_template("addtask.html")

@app.route("/addtask", methods=["POST"])
def add_task():
  task = request.form.get("task")
  tasks.append(task)
  print(tasks)
  return redirect(url_for("task_list"))

