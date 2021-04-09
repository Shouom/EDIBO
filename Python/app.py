from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	return "<h1>Hello you!</h1>"

if __name__ == '__main__':
    app.run(port=5000)

ufile = open('user.txt','r')
pfile = open('password.txt','r')

app.config['MYSQL_USER'] = ufile.read()
ufile.close()
app.config['MYSQL_DB'] = 'world'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)