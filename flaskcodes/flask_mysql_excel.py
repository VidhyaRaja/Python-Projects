import pymysql  # connecting mysql with excel
import io  # input output module to convert the table into excel
import xlwt  # it predefined ms excel module
from flask import Flask, Response, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'empdb'
mysql.init_app(app)


@app.route('/')
def upload_form():
    return render_template('home1.html')


@app.route('/download/report/excel')
def download_report():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT ename,pwd FROM emptab")
    result = cursor.fetchall()
    output = io.BytesIO()
    workbook = xlwt.Workbook()
    sh = workbook.add_sheet('empdata')
    sh.write(0, 0, 'empname')
    sh.write(0, 1, 'password')

    idx = 0
    for row in result:
        sh.write(idx + 1, 0, str(row['ename']))
        sh.write(idx + 1, 1, row['pwd'])
        idx += 1
    workbook.save(output)
    output.seek(0)
    cursor.close()
    conn.close()
    return Response(output, mimetype="application/ms-excel",
                    headers={"Content-Disposition": "attachment;filename=employee_report.xls"})


if __name__ == "__main__":
    app.run()