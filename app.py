from flask import Flask, render_template
from dotenv import load_dotenv
from src.config import Config
from flask_bootstrap import Bootstrap


load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')
