from flask import Flask, render_template, url_for
import os

# creates a Flask application, named app
app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
                   for root_path, dirs, files in os.walk(folder)
                   for f in files))

# a route where we will display a welcome message via an HTML template
@app.route("/")
@app.route("/index")
def index():
    message = "poo"
    return render_template('index.html', message=message, last_updated=dir_last_updated('static'))
    
# run the application
if __name__ == "__main__":
    app.run(debug=True)
