from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recent/')
def recent():
    return render_template('recent.html')

if __name__ == "__main__":
    app.run(debug=True)