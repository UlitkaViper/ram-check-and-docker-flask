from db import get_db

from flask import render_template, Blueprint, request, Request


user_blueprint = Blueprint("user", __name__, url_prefix="/user")


def get(db, request: Request):
    user = db.user.find_one({'name': request.args["nm"]})
    if user:
        msg = f"Пользователь {user.get('name')}, возраст: {user.get('age')}"
    else:
        msg = "Такого пользователя не существует"

    return msg


def post(db, request):
    db.user.insert_one({'name': request.form["post_name"], 'age': request.form["post_age"]})
    msg = f"Добавлен пользователь {request.form['post_name']}"

    return msg


def put(db, request):
    new_val = {"$set": {'age': request.form["put_age"]}}
    updated = db.user.update_one({'name': request.form["put_name"]}, new_val, upsert=False)
    if updated.matched_count:
        msg = f"У пользователя {request.form['put_name']} возраст изменен на {request.form['put_age']}"
    else:
        msg = "Такого пользователя не существует"
    
    return msg


@user_blueprint.route("/", methods=["GET", "POST", "PUT"])
def user():
    db = get_db()
    if request.method == "GET":
        msg = get(db, request)
        return render_template("base.html", result=msg, name=request.args["nm"])
    if request.method == "POST":
        msg = post(db, request)
        return render_template("base.html", result=msg)
    if request.method == "PUT":
        msg = put(db, request)
        return {"result": msg}
