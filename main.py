from flask import Flask, request, render_template
import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ("mysql+pymysql://root:6206086329@bittu/blogforyou")
db = SQLAlchemy(app)


class Contacts(db.Model):
    srno = db.column(db.integer, primary_key=True)
    name = db.column(db.string(20), nullable=False)
    email = db.column(db.string(20), nullable=False)
    message = db.column(db.string(120), nullable=False)
    date = db.column(db.string(12), nullable=False)
    phone_number = db.column(db.string(25), nullable=False)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        """"add entry to database"""
        name = request.form.get('name'),
        email = request.form.get('email'),
        message = request.form.get('message')
        phone_number = request.form.get('phone'),
        entry = Contacts(name=name, email=email, message=message, phone_number=phone,)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


@app.route('/post.html')
def post():
    return render_template('post.html')


app.run(debug=True)
