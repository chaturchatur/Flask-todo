from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")
todos = [{"task":"Sample", "done":False}]

@app.route("/")
def home():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form['todo']
    todos.append({"task":task, "done":False})
    return redirect(url_for("home"))

@app.route("/edit/<int:index>", methods=["POST", "GET"])
def edit(index):
    if request.method == "POST":
        todos[index]['task'] = request.form['todo']
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", todos=todos, index=index)
    
@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("home"))
    
@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("home"))
    
    
if __name__ == "__main__" :
    app.run(debug=True)