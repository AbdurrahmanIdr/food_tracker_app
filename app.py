from flask import Flask

app = Flask(__name__)
app.config['DEBUG']=1
app.config['PORT']=5000
app.config['HOST']='0.0.0.0'
app.config['SECRET_KEY'] = 'almeida-secret-key'


@app.route('/')
def home():
    return "Hello, Flask!"


if __name__ == '__main__':
    app.run()
    