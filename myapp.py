from flask import Flask, render_template, request, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY']= "My super secret key"
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{username}:{password}@{server}/testdb".format('shukri', 'Password1234/', 'myservershukri1.database.windows.net')


#SQLALCHEMY_DATABASE_URI = 'mysql://user@mysqlsvr:pass1234@mysqlsvr.mysql.database.azure.com:3306/flask_db?ssl_ca=BaltimoreCyberTrustRoot.crt.pem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://shukri@shukriserversql:Password1234/@shukriserversql.mysql.database.azure.com:3306/flask_db?ssl_ca=BaltimoreCyberTrustRoot.crt.pem'
db = SQLAlchemy(app)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Owner(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    forename = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    pet = db.relationship('Pet',backref ='all_pet')

class pet(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    type = db.Column(db.String(20))
    owner_id = db.Column(db.Integer,db.ForeignKey('own_id)'))

'''
db.create_all()
o1 = Owner(id=1, forename='John', surname='Martin' )
o2 = Owner(id=2, forename='Lucy', surname='Johnson' )
o3 = Owner(id=3, forename='Rob', surname='Graham' )
o4 = Owner(id=4, forename='Linda', surname='Joned' )
db.session.add(o1)
db.session.add(o2)
db.session.add(o3)
db.session.add(o4)
db.session.commit()
p1 = Owner(id=1, name='Doggie', type='Dog', owner_id=1)
p3 = Owner(id=3, name='Olive',  type='Rabbit', owner_id=1)
p2 = Owner(id=2, name='Bella', type='Hamster' , owner_id=2)
p4 = Owner(id=4, name='Max',  type='Cat', owner_id=2)
p5 = Owner(id=5, name='Cooper', type='Dog', owner_id=3)
p6 = Owner(id=6, name='Daisy', type='Snake', owner_id=4)
p7 = Owner(id=7, name='Luna', type='Cat', owner_id=4)
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)
db.session.add(p6)
db.session.add(p7)
db.session.commit()

'''

class SignUpForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')
    location = StringField ('Enter Chosen Location')
    submit = SubmitField('Sign Up')



@app.route('/')
def home():
    return "Hello World!"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html',result=result)
    return render_template('signup.html',form=form)

if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=5000, debug=True) 
