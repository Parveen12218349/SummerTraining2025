from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    html_content = ("<html><body>"
                    "<h1>My first flask page</h1>"
                    "<p>to tukruke mutu hera</p>"
                    "</body></html>")
    return html_content

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


if __name__ == '__main__':
    app.run()
