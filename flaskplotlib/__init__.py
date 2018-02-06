from flask import Flask
from flaskplotlib.views import client


app = Flask(__name__)
app.register_blueprint(client)
app.config.from_object('flaskplotlib.config')
