from flask import session,flash,request,Flask,render_template, redirect,url_for, session, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_PORT"]=3306
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="myflaskapp"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

app.secret_key = 'super secret key'


# initial MySQL

mysql=MySQL()
try:
    mysql.init_app(app)
except Exception as e:
    print(e)
@app.route("/")
def index():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
# multiple Articles
@app.route("/articles")
def articles():
    cur=mysql.connection.cursor()
    result=cur.execute("SELECT * from articles")
    articles=cur.fetchall()
    cur.close()
    if result>0:
        return render_template("articles.html",articles=articles)
    else:
        msg ="No Article Found"
        return render_template("articles.html",msg=msg)

# single Article
@app.route("/article/<string:id>/")
def article(id):
    cur=mysql.connection.cursor()
    result=cur.execute("SELECT * from articles where id=%s",[id])
    article=cur.fetchone()
    cur.close()

    return render_template("article.html",article=article)


@app.route("/logout")
def logout():
    session.clear()
    flash("you are now logged out","success")

    return redirect(url_for("login"))
def is_loggedin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args,**kwargs)
        else:
            flash ("Unauthorized ,Please logged in", "danger")
            return redirect(url_for("login"))
    return wrap

@app.route("/dashboard")
@is_loggedin
def dashboard():
    cur=mysql.connection.cursor()
    result=cur.execute("SELECT * from articles")
    articles=cur.fetchall()
    cur.close()
    if result>0:
        return render_template("dashboard.html",articles=articles)
    else:
        msg ="No Article Found"
        return render_template("dashboard.html",msg=msg)
    # register form Class
@app.route("/edit_article/<string:id>",methods=["GET","POST"])
@is_loggedin
def edit_article(id):
#create cursor
    cur=mysql.connection.cursor()
    #Get Article by ID
    result=cur.execute("SELECT * FROM articles WHERE id=%s",[id])
    #commit connection
    article=cur.fetchone()
    #GET form

    form= ArticleForm(request.form)
    #populate article form fields
    form.title.data=article["title"]
    form.body.data=article["body"]

    if request.method=="POST" and form.validate():
        title=request.form["title"]
        body=request.form["body"]

        cur.execute("UPDATE articles set title=%s ,body=%s WHERE id=%s ",(title,body,id))
        mysql.connection.commit()
        #close connection
        cur.close()
        flash("Article Updated","success")
        return redirect(url_for('dashboard'))


    return render_template("edit_article.html",form=form)

# delete article
@app.route("/delete_article/<string:id>",methods=["GET","POST"])
@is_loggedin
def delete_article(id):
    #create cursor
    cur=mysql.connection.cursor()
    #delete Article by ID
    result=cur.execute("DELETE  FROM articles WHERE id=%s",[id])
    #commit connection
    flash("Article DELETED","danger")
    mysql.connection.commit()
    #close connection
    cur.close()

    return redirect(url_for('dashboard'))


class RegisgterForm(Form):
    name=StringField("Name",[validators.Length(min=1,max=50) ,validators.DataRequired()])
    username=StringField("Username",[validators.Length(min=4,max=25),validators.DataRequired() ])
    email=StringField("Email",[validators.Length(min=6,max=50) ,validators.DataRequired()])
    password=PasswordField("Password",[
    validators.DataRequired(),
    validators.EqualTo('confirm',message="passwords do not match"),
    validators.Length(min=1,max=50) ])
    confirm=PasswordField('Confirm password',[validators.DataRequired()])


# register form Class
class ArticleForm(Form):
    title=StringField("Title",[validators.Length(min=1,max=100) ,validators.DataRequired()])
    body=TextAreaField("Body",[validators.Length(min=30),validators.DataRequired() ])
@app.route("/add_article",methods=["GET","POST"])
@is_loggedin
def add_article():
    form= ArticleForm(request.form)
    if request.method=="POST" and form.validate():
        title=form.title.data
        body=form.body.data
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO articles(title, body,author) Values(%s,%s,%s)",(title,body,session["username"]))
#commit connection
        mysql.connection.commit()
        #close connection
        cur.close()
        flash("Article Created","success")
        return redirect(url_for('dashboard'))
    return render_template("add_article.html",form=form)


@app.route("/register",methods=["GET","POST"])
def register():
    form=RegisgterForm(request.form)
    if request.method=="POST" and form.validate():
        name=form.name.data
        email=form.email.data
        username=form.username.data
        password=sha256_crypt.hash(form.password.data)
        #cursor create
        try:
            cur= mysql.connection.cursor()
            cur.execute("INSERT INTO `users` ( `name`, `username`, `email`, `password`, `DateTime`) VALUES (%s,%s,%s,%s,CURRENT_TIMESTAMP)",(name,email,username, password))
            mysql.connection.commit()
            cur.close()
        except Exception as e:
            print(e)
        flash("You are now register and can log in",'success')

        redirect(url_for('index'))


    return render_template("register.html",form=form)
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        # get forms fields
        try:
            username=request.form["username"]
            password_candidate=request.form["password"]
            cur= mysql.connection.cursor()
            result=cur.execute("SELECT * from `users` where `username`='{0}'".format(username))
            if result>0:
                data=cur.fetchone()
                password=data["password"]
                # compare passwords
                if sha256_crypt.verify(password_candidate,password):
                    # password match
                    session["logged_in"]=True
                    session["username"]=username
                    flash("you are now logged in","success")
                    return redirect(url_for("dashboard"))

                else:
                    error="Invalid Login"
                    return render_template("login.html",error=error)

            else:
                error="Username not found"
                return render_template("login.html",error=error)
            mysql.connection.commit()
            cur.close()
        except Exception as e:
            print(e)


    return render_template("login.html")
if __name__=="__main__":
    app.run(debug=True)
