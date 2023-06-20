from flask import Flask, render_template,

from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class Contact(db.Model):
    id= db.column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    subject = db.Column(db.String(200))
    email = db.Column(db.String(200))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/thankyou', methods =['POST'])
def thankyou():
    name = request.form['name']
    email = request.form['email']
    subject = request.form ['subject']
    message = request.form['message']

    data = Contact (name=name,email=email,subject=subject,message='message')
    db.session.add(data)
    db.session.commit()
    return redirect (url_fro('home'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)
