from flask import render_template, Flask
from datafoo import congress

app = Flask(__name__)
congressmembers = congress.get_legislators()



@app.route('/')
def homepage():
    oldtoyoung = sorted(congressmembers, key=lambda x: x['bio']['birthday'])
    html = render_template('homepage.html', legislators=oldtoyoung)
    return html


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)


