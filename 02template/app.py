from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hellotemplate.html')

@app.route('/about_me/<first_name>/<last_name>')
def about(first_name, last_name):
    return render_template('abouttemplate.html', first_name=first_name,last_name=last_name)

# "magic code" , boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)