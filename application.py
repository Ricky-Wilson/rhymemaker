# The MIT License (MIT)

# Copyright (c) 2013 Yat Choi

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from flask import Flask
from flask import render_template, url_for, request, jsonify, Response
import RhymeMaker
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('home.html', word=[], rhymes=[])

@app.route('/pad')
def pad():
	return render_template('pad.html', word=[], rhymes=[])

@app.route('/rhyme')
def ajax_rhyme():
	word = request.args.get('word','')
	rhymes = RhymeMaker.rhyme(word,75)
	# return render_template('home.html', word=word, rhymes=rhymes)
	return json.dumps(rhymes)

if __name__ == '__main__':
    app.run(debug=True)