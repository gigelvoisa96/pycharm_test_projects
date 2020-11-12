from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return 'hello world'

if __name__ == '__main__':
    app.add_url_rule('/', 'hello', hello_world)
    app.run(debug=True)
