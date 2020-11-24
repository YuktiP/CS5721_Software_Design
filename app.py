from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

#config db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method =='POST':
        log_reg = request.form
        if log_reg['button'] == 'login':
            return redirect('/login')
        elif log_reg['button'] == 'register':
            return redirect('/register')
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method =='POST':
        userDetails = request.form
        name = userDetails['name']
        phonenumber = userDetails['phonenumber']
        address = userDetails['address']
        email = userDetails['email']
        dateofbirth = str(userDetails['dateofbirth'])
        print(len(dateofbirth))
        occupation = userDetails['occupation']
        income = userDetails['income']
        username = userDetails['username']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO userdetails(name,phonenumber,address,email,dateofbirth,occupation,income,username,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name,phonenumber,address,email,dateofbirth,occupation,income,username,password))
        mysql.connection.commit()
        cur.close()
        return "<h1>Registered</h1>"
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        #fetch data from form
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        #password2 = cur.execute("SELECT password FROM userdetails WHERE username = %s", username,)
        sql = "SELECT password FROM userdetails WHERE username = %s"
        adr = (username, )
        cur.execute(sql, adr)
        myresult = cur.fetchall()
        print(myresult)
        if myresult[0][0] == password:
            cur.close()
            return "<h1>Logged In</h1>"
        else:
            return "<h1>Invalid!!! Please try Again.</h1>"
    return render_template('login.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue =cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails =cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)

 #INSERT INTO userdetails(name,phonenumber,address,email,dateofbirth,occupation,income,username,password) values('praveen','7760433849','xyz','pavit1807@gmail.com','18/07/1996','student','10000000','praveentalavar','qwerty');