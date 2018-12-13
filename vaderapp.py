from flask import Flask, request, render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

analyzer = SentimentIntensityAnalyzer()

class Sentence(object):
    def __init__(self, text):
        text = text.strip()
        self.text = text
        self.scores = analyzer.polarity_scores(text)


@app.route('/')
def main():
    return render_template('view.html')


@app.route('/', methods=["POST"])
def analyze():
    text = request.form.get('textbox').strip()
    split = request.form.get('split')
    text = text.strip().replace('\r\n', '\n').replace('\r', '\n')
    if split == 'line':
        sents = text.split('\n')
    else:
        sents = text.split('\n\n')

    sents = [Sentence(sent) for sent in sents]
    return render_template('view.html', sents=sents)



