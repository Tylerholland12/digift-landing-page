from application.controllers.home import home
from application.controllers.user_login import login_route
from flask import Flask


app = Flask("digift", template_folder='application/templates',
            static_folder='application/static',
            instance_relative_config=True)

app.register_blueprint(home)
app.register_blueprint(login_route)


def get_email():
    # new_user = User(
    #     request.form['email'], request.form['password'])

    if request.method == 'POST':
        email_user = user.insert_one({'email': request.form['email']})



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)
