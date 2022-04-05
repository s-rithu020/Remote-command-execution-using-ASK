import flask
from flask_ngrok import run_with_ngrok
import flask.views
import datetime
import os
import functools

app = flask.Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/time')
def hi():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'HELLO!',
        'time' : timeString
        }
    return flask.render_template('time.html', **templateData)

@app.route('/cakes')
def cakes():
    return flask.render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    return flask.render_template('page.html', name=name)

'''@app.route('/music/')
def download_file(tune):
    return send_from_directory('/home/name/Music/', tune)'''

class Music(flask.views.MethodView):
    def get(self):
        songs = os.listdir('static/music')
        return flask.render_template("music.html", songs=songs)
    

app.add_url_rule('/music/',
                 view_func=Music.as_view('music'),
                 methods=['GET'])

class Display(flask.views.MethodView):
    def get(self):
        return flask.render_template('echo.html')
    def post(self):
        return str(flask.request.form['expression'])

app.add_url_rule('/echo/',
                 view_func=Display.as_view('echo'),
                 methods=['GET','POST'])


if __name__ == '__main__':
    #app.run(debug=True, port=80, host='0.0.0.0')
    app.run()
