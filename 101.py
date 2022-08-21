from flask import Flask,request,render_template
import mysql.connector
app=Flask(__name__)


def log_request(req:'flask_request') ->None:
    mydb=mysql.connector.connect(host= 'localhost', user= 'root',password='6206086329@bittu',database='blogforyou')
    mycursor = mydb.cursor()
    SQL = """insert into contact(
        name,email,phone_number,message)
        values
        (%s,%s,%s,%s)"""
    mycursor.execute(SQL, (request.form.get('name'),
                           request.form.get('email'),
                           request.form.get('phone'),
                           request.form.get('message')))
    mydb.commit()


@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html',methods=['GET','POST'])
def contact():

    if (request.method=='POST'):
         """"add entry to database"""
         name=request.form.get('name'),
         email=request.form.get('email'),
         phone_number=request.form.get('phone'),
         message=request.form.get('message')
    log_request(request)

    return render_template('contact.html')


@app.route('/post.html')
def post():
    return render_template('post.html')


app.run(debug=True)