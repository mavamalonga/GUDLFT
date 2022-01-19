from flask import Flask

app = Flask(__name__)
app.secret_key = 'something_special'

from app import routes