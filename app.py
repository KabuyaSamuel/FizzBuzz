from flask import Flask, render_template

app = Flask(__name__)

@app.route('/fizzbuzz')
def fizzbuzz():
    return render_template('fizzbuzz.html', numbers=range(1, 101))

if __name__ == '__main__':
    app.run()