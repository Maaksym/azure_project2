from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Инициализация базы данных в виде списка словарей
db = []

@app.route("/")
def home():
    return render_template("base.html", todo_list=db)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = {"id": len(db) + 1, "title": title, "complete": False}
    db.append(new_todo)
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    for todo in db:
        if todo["id"] == todo_id:
            todo["complete"] = not todo["complete"]
            break
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    for todo in db:
        if todo["id"] == todo_id:
            db.remove(todo)
            break
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()