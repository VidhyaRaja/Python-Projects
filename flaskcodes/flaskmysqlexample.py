from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'empdb'
mysql.init_app(app)


@app.route('/')
def sample():
    return render_template("home1.html")


@app.route('/login', methods=['POST', 'GET'])
def gayathri():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        con = mysql.connect()
        cur = con.cursor()
        cur.execute("select * from emptab where ename='"+username+"'and pwd='"+password+"'")
        data = cur.fetchone()
        if data is None :
            return "Invalid username and password"
        else:
            return render_template("sampl.html")
    else:
        return render_template("gayathri.html")


if __name__ == "__main__":
    app.run()
