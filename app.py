# Importing flask module in
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, abort

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# Define the allowed hosts
ALLOWED_HOSTS = ['mompopapp.herokuapp.com', 'www.softwaterlabs.dev']

# Middleware to check if the request's host is allowed
@app.before_request
def restrict_host():
    host = request.host
    if host not in ALLOWED_HOSTS:
        abort(403)  # Forbidden access if host is not in ALLOWED_HOSTS

# Best practice for dynamic abilities, key values (rule or path, endpoint, view function)
def test_func(name):
    return f"My name is {name} and I am a python developer."

app.add_url_rule('/<name>', 'name_page', test_func)

@app.route('/')
def index():
    return render_template('index.html')

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
