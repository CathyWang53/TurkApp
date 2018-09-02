from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/test')
    def test():
        return 'hello, world!'

    from . import welcome
    app.register_blueprint(welcome.bp)

    from . import s1_v2
    app.register_blueprint(s1_v2.bp)
    
    from . import tutorial
    app.register_blueprint(tutorial.bp)

    return app
