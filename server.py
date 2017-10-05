import re

from flask import Flask, render_template, request

app = Flask(__name__)
NBSP = '\u00A0'
RULES = {
    'quotes': (r'''(['"])(.*?)(\1)''', r'«\2»'),
    'm-hyphen': (r' - ', r' — '),
    'hyphen_between_number': (r'(?<=\d)(-)(?=\d)', r'‒'),
    'space_after_number': (r'(?<=\d)(\s)(?=[\D])', NBSP),
    'extra_space': (r' {2,}', r' '),
    'extra_new_line': (r'\r\n{2,}', r'\r\n'),
    'space_with_conjunktion': (r'(?<=(?<=\s[а-яА-Я]{2})|(?<=\s[а-яА-Я]{1}))(\s)(?=.)', NBSP)
}


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        text = request.form['text']
        return render_template('form.html', text=text, result=typograf(text))


def typograf(text):
    for rule in RULES.values():
        text = re.sub(rule[0], rule[1], text)
    return text


if __name__ == "__main__":
    app.run()
