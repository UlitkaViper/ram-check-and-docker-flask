from flask import Flask

app = Flask(__name__)


def register_apps():
    from views import user_blueprint, home_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(user_blueprint)


if __name__ == "__main__":
    register_apps()
    app.run(host="0.0.0.0", debug=True, port=8080)
