import os
from flask import Flask, make_response, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods = ['GET'])
def wave():
    name = request.args['name']

    return f"I am waving at {name}"

@app.route('/count_vowels', methods = ['POST'])
def count_vowels():
    text = request.form['text']

    vowels = 0
    for letter in text:
        if letter in 'aeiou':
            vowels += 1

    return f'There are {vowels} vowels in "{text}"'



@app.route('/sort-names', methods = ['POST'])
def sort_names():
    if "names" not in request.form:
        response = make_response("Bad Request - Please provide names!")
        response.status_code = 400
        return response
        # return "Please provide names!"
    
    
    names = request.form['names']
    all_names = names.split(',')
    all_names.sort()
    return ",".join(all_names)



@app.route('/names', methods = ['GET'])
def add_names():
    if "add" not in request.args:
        response = make_response("Bad Request - Please provide a name!")
        response.status_code = 400
        return response

    names = ["Julia", "Alice", "Karim"]
    add = request.args['add']

    if add != "":
        names += add.split(',')
    
    names.sort()

    return ", ".join(names)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

