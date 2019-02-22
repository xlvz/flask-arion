from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """docstring for index"""
    return render_template('index.html')

#@app.route('/l')
@app.route('/lokality/<lokalita>')
def lokality(lokalita):
    """docstring for lokality"""
    return render_template('lok.html', lokalita = lokalita)

if __name__ == '__main__':
    app.run()
