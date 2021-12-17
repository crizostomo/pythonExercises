from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/query-example', methods = ["POST", "GET"])
def query_example():
    language = request.args.get('language')

    # if key doesn't exist, returns a 400, bad request error
    framework = request.args['framework']

    # if key doesn't exist, returns None
    website = request.args.get('website')

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        return '''
                  <h1>Your name is: {}</h1>
                  <h1>You are: {}</h1>'''.format(name, age)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>name: <input type="text" name="name"></label></div>
               <div><label>age: <input type="text" name="age"></label></div>
               <input type="submit" value="Submit">
           </form>'''

@app.route('/json-example', methods = ["POST", "GET"])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)