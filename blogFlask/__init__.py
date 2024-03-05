from flask import Flask

app = Flask(__name__)

from blogFlask.views import index
