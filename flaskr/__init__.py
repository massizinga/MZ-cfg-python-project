import os

from flask import Flask, render_template, request



def create_app(test_config=None):
    print("got into create_app()!")
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/")
    def say_hello():

        return render_template("index.html")
    
    @app.route("/create")
    def create_patient():
        return render_template("create.html")
    
    @app.route('/post-create', methods = ['POST'])
    def post():
        text = request.form['first_name']
        processed_text = text.upper()
        return processed_text

    from . import db
    db.init_app(app)
    

    
    return app

