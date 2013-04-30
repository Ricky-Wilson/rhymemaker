from flask import Flask
from flask import render_template, url_for, request, jsonify, Response
import rhymemaker
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('home.html', rhymes=[])

@app.route('/rhyme')
def ajax_rhyme():
	word = request.args.get('word','')
	rhymes = rhymemaker.rhyme(word,20)
	return render_template('home.html', rhymes=rhymes)

if __name__ == '__main__':
    app.run(debug=True)