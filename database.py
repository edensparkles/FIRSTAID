import pymongo
from pymongo import MongoClient
from flask import Flask
import datetime
client = MongoClient()

client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
collection = db.test_collection

users = db.users
user = {"dob" = request.form['dob'],
    "name" = request.form['name'],
    "number"=request.form['number'],
    "emai l"=request.form['email'],
    "password"=request.form['password'],
    "contact1_num"=request.form['contact1_num'],
    "contact2_num"=request.form['contact2_num'],
    "contact1"=request.form['contact1'],
    "contact2"=request.form['contact2']
        }
        

users.insert_one(user)

app = Flask(__name__)

html = """<form action="your_method_name" method="post">
    Project file path: <input type="text" name="projectFilepath"><br>
    <input type="submit" value="Submit">
</form>"""


@app.route('/index.html/', methods=['POST'])
def handle_data():
    projectpath = request.form.projectFilePath

@app.route('/new_user/', methods=['POST'])
def signup():
    
    if not session.get(' dob','name', 'number', 'email', 'password'):
        abort(401)
    new_user = {"dob": dob,
    "name": name,
    "number": number,
    "email": email,
    "password": password
            }
    db.insert_one(new_user)
    flash('Account successfully created')
    return redirect('opening.html', dob=dob, name=name, number=number, email=email, password=password, contact1_num=contact1_num, contact2_num=contact2_num, contact1=contact1, contact2=contact2) 
        
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect ('opening.html')
@app.route('/login')
def do_admin_login():
    if request.form['password']=='password' and request.form['name']=='admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return redirect ('opening.html')
    
if __name__ == '__main__':
    app.run()