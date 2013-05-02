from flask import Flask
from flask import render_template, url_for, request, jsonify, Response
import RhymeMaker
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('home.html', word=[], rhymes=[])

@app.route('/rhyme')
def ajax_rhyme():
	word = request.args.get('word','')
	rhymes = RhymeMaker.rhyme(word,75)
	# return render_template('home.html', word=word, rhymes=rhymes)
	return json.dumps(rhymes)

if __name__ == '__main__':
    app.run(debug=True)