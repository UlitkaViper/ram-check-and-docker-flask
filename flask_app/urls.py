from app import app
from views import UserView


app.add_url_rule("/user/", view_func=UserView.as_view("user"))