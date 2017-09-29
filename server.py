import re

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        text = request.form['text']
        return render_template('form.html', text=text, result=typograf(text))


def typograf(text):
    nbsp = '\u00A0'
    text = re.sub(r'''(['"])(.*?)(\1)''', r'«\2»', text)
    text = re.sub(r' - ', r' — ', text)
    text = re.sub(r'(?<=\d)(-)(?=\d)', r'‒', text)
    text = re.sub(r'(?<=\d)(\s)(?=[\D])', nbsp, text)
    text = re.sub(r' {2,}', r' ', text)
    text = re.sub(r'\r\n{2,}', r'\r\n', text)
    text = re.sub(r'(?<=(?<=\s[а-яА-Я]{2})|(?<=\s[а-яА-Я]{1}))(\s)(?=.)', nbsp, text)
    return text


if __name__ == "__main__":
    app.run()
