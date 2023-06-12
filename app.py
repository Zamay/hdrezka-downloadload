from flask import Flask, render_template, request
from HdRezkaApiChatGPT import HdRezkaApi

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        rezka = HdRezkaApi(url)
        result = rezka.getStream()('720p')
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
