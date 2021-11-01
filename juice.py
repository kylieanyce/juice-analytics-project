from flask import Flask, render_template
import requests
import json
import csv


app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route("/", methods=['GET', 'POST'])
def get_juice():
    my_headers = {'x-app-id': '4065bc15',
                  'x-app-key': f'{app.config.get("MY_API_KEY")}',
                  'x-remote-user-id': '0'}
    response = requests.get(
        "https://nutritionix.com/nixapi/brands/51db37d0176fe9790a899db2/items/1?limit=60", headers=my_headers)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
        return response.json()
    data = response.content
    return render_template("juice.html", data=data)


if __name__ == '__main__':
    app.run(host='', port=5000, debug=True)
