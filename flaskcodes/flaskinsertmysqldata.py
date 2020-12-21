from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'empdb'
mysql.init_app(app)


@app.route("/",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['n']
        email = request.form['e']
        password=request.form['p']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("INSERT INTO registration(empname,mail,pwd) VALUES (%s,%s,%s)", (name, email, password))
        con.commit()
        return ('Registration completed successfully')
    else:
        return render_template("register.html")


if __name__=="__main__":
    app.run()