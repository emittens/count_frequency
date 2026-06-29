from flask import Flask, render_template, request 
import re 

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    word_count = {}

    if request.method == 'POST':
        text = request.form['text']

        text = text.lower()

        text = re.sub(r'[^a-z0-9\s]','',text)

        words = text.split()

        for word in words:
            if word in word_count:
                word_count[word] += 1

            else: 
                word_count[word] = 1

    return render_template('index.html', word_count=word_count)

if __name__=='__main__':
    app.run(debug=True)