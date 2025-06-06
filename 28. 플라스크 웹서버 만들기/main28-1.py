from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome this place"

@app.route('/favicon.ico') 
def favicon(): 
    return url_for('static', filename='./static/favicon.ico')

@app.route('/map')
def map():
    return render_template("uni_map.html")

def main():
    app.run(debug=False, port=80)
    
if __name__== '__main__':
    main()