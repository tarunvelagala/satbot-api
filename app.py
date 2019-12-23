from flask import Flask, jsonify, render_template, request, make_response
import urllib
import json
import os

app = Flask(__name__)

companies = [
    {
        'id': 1, 'company_name': 'Cognizant',
        'drive_date': '2019-01-12'
    },
    {
        'id': 2,
        'company_name': 'Google',
        'drive_date': '2019-03-12'
    }
]


@app.route('/')
def hello_world():
    return 'Helloworld'


@app.route('/satbot-api/v1.0/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))


@app.route('/satbot-api/v1.0/drivedetails/<company_name>', methods=['GET'])
def get_details(company_name):
    for i in companies:
        for k, v in i.items():
            if v == str(company_name):
                print(v)
                return jsonify({'results': i['drive_date'], 'status': 'OK'})
    else:
        return jsonify({'results': None, 'status': 'NOT OK'})


if __name__ == '__main__':
    app.run()
