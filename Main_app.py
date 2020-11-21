from flask import Flask, render_template,request , session , redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
from werkzeug.utils import secure_filename
import json,os,math

port = int(os.environ.get('PORT',5000))


with open('config.json','r') as c:
    params=json.load(c)['Params']

local_server=params['local_server']

app = Flask(__name__)
app.config['Upload_File']=params['upload_location']
app.secret_key = "super_secret_key"

#Setting up the connection to Smtp for sending mail using Flask-Mail (Module)
app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT ='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['user_mail'],
    MAIL_PASSWORD=params['user_password']
)
mail=Mail(app)

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_id"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["Prod_id"]

#connecting to database using SQLAlchemy
db = SQLAlchemy(app)

# Create Class for database
class Contacts(db.Model):
    '''
    SNo	NAME	EMAIL	Phone	MESSAGE	DATE
    Define all the columns of the database..
    '''

    SNo = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String(20), nullable=False)
    EMAIL = db.Column(db.String(20),  nullable=False)
    Phone = db.Column(db.String(12), nullable=False)
    MESSAGE = db.Column(db.String(120),  nullable=False)
    DATE = db.Column(db.String(20),  nullable=True)


class Posts(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(25), nullable=False)
    Slug = db.Column(db.String(20), nullable=False)
    Content = db.Column(db.String(120), nullable=False)
    Subtitle = db.Column(db.String(12), nullable=False)
    Date = db.Column(db.String(10), nullable=True)
    img_name = db.Column(db.String(12), nullable=True)



@app.route('/')
def home():
    page=request.args.get('page')
    posts=Posts.query.filter_by().all()
    last=len(posts)/params["no_of_post"]
    last=math.ceil(last)

    if not (str(page).isnumeric()):
        page=1
    page=int(page)
    # Pagination Logic
    posts=posts[(page-1)*int(params["no_of_post"]):(page)*int(params["no_of_post"])]

    if page==1:
        prev="#"
        next="/?page="+str(page+1)
    elif page==last:
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)


    return render_template('index.html',params=params,posts=posts,prev=prev,next=next)

@app.route('/about')
def about():
    return render_template('about.html',params=params)



@app.route('/dashboard', methods=['GET','POST'])
def Dashboard():
    posts=Posts.query.all()
    # Check if user is already logged in or not
    if ( 'user' in session and session['user']== params['admin_id'] ):
        return render_template('dashboard.html',params=params,posts=posts)

    if (request.method)=='POST':
        username=request.form.get('Email')
        password=request.form.get('Password')
        if (username==params['admin_id'] and password==params['admin_password']):
            session['user']=username #use session variable to store the status of dashboard
            return render_template('dashboard.html',params=params,posts=posts)

    return render_template('login.html',params=params)

@app.route("/edit/<string:Sno>", methods=['GET','POST'])
def edit(Sno):
    if ('user' in session and session['user'] == params['admin_id']):
        if (request.method) == 'POST':
            box_Title=request.form.get('Title')
            Slug=request.form.get("Slug")
            Subtitle=request.form.get("Sub_title")
            Content=request.form.get("Content")
            Image_file=request.form.get("img_file")
            date=datetime.now()

            # Adding New post
            if Sno=='0':
                post=Posts(Title=box_Title,Slug=Slug,Content=Content,Subtitle=Subtitle,img_name=Image_file,Date=date)
                db.session.add(post)
                db.session.commit()

            else:
                post=Posts.query.filter_by(SNo=Sno).first()
                post.Title=box_Title
                post.Slug=Slug
                post.Content=Content
                post.Subtitle=Subtitle
                post.img_name=Image_file
                post.Date=date
                db.session.commit()
                return  redirect("/edit/"+Sno)

        post = Posts.query.filter_by(SNo=Sno).first()
        return  render_template("edit.html",params=params,post=post , Sno=Sno)

@app.route("/uploader", methods=['GET','POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_id']):
        if (request.method) =="POST":
            f=request.files['file1']
            f.save(os.path.join(app.config['Upload_File'],secure_filename(f.filename)))
            # for Secure_filename read from Flask documentation
            return "Uploaded Successfully"

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route("/delete/<string:Sno>", methods=['GET','POST'])
def delete(Sno):
    if ('user' in session and session['user'] == params['admin_id']):
        post=Posts.query.filter_by(SNo=Sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dashboard')


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    slug2 = str(post_slug)
    post = db.session.query(Posts).filter_by(Slug = slug2).first()
    return render_template('post.html', params=params, post=post)

@app.route('/contact',methods=["GET","POST"])
def contact():
    if (request.method)=='POST':

        # Fetching details from Html ..
        name=request.form.get('name')
        email=request.form.get('Email')
        phone=request.form.get('phone')
        message=request.form.get('message')

        '''
        SNo	NAME	EMAIL	Phone	MESSAGE	DATE
        '''
        entry=Contacts(NAME=name,EMAIL=email,Phone=phone,MESSAGE=message,DATE=datetime.now())

        #add entry to database
        db.session.add(entry)
        db.session.commit()

        # Sending the actual part of Mail...(title,sender_mail,recipients,body)..open flask-Mail for more Info
        mail.send_message(
            "Attention ! New Message From Blog",
            sender=email,
            recipients=[params['user_mail']],
            body=message+ '\n' +phone
        )

    return render_template('contact.html',params=params)

#Helps to run the server
app.run(port=port, debug=True)
