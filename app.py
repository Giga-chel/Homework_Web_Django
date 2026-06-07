from flask import Flask, render_template, request
from dotenv import load_dotenv
from src.config import Config
from flask_bootstrap import Bootstrap
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        # Сервер принимает POST-запрос, данные выводятся в консоль без ошибок
        data = request.form.get('message') or request.get_json()
        print(f"Получены данные: {data}")
        return render_template('contacts.html', message_sent=True)

    # Чтение файла происходит с помощью контекстного менеджера
    contacts_list = []
    try:
        with open('contacts.txt', 'r', encoding='utf-8') as file:
            contacts_list = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        contacts_list = ["Файл contacts.txt не найден"]

    return render_template('contacts.html', contacts=contacts_list)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/post', methods=['POST'])
def post_request():
    # Сервер принимает POST-запрос, данные выводятся в консоль без ошибок
    data = request.get_json()
    print(f"POST-запрос получен: {data}")
    return 'POST-запрос принят', 200


if __name__ == '__main__':
    app.run(debug=True)
