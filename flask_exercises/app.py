from flask import Flask, request
import random
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route('/welcome', methods=["POST", "GET"])
def home():
    print(request.data)
    return "Hello, welcome to this page"

@app.route('/random', methods = ["POST", "GET"])
def draw():
   print(request.values) #Values?
   num = random.randint(0, 5)
   return str(num)

@app.route("/sptime", methods = ["POST", "GET"])
def sptime():
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone("America/Sao_Paulo")
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    return data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")

@app.route("/date", methods = ["POST", "GET"])
def data():
    date = datetime.now()
    print(date)
    return date.strftime("%d/%m/%y")


#https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
#https://stackoverflow.com/questions/45385188/flask-cant-get-post-data-from-postman-or-web-page-but-work-in-python-request
@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)

if __name__ == '__main__':
    app.run()

#Challenge: In this project, input info from user. (i) By browser and (ii) postman
