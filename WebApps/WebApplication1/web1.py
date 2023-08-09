from flask import Flask, render_template

app = Flask(__name__)
# page_name = "data.html"
@app.route('/')
def render_static():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)