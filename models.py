from app import db
#from flask_mysqldb import MySQL

class Customer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    FIRSTNAME=db.Column(db.String(20))
    SURNAME=db.Column(db.String(20))
    ADDRESS=db.Column(db.String(20))
    
    def __init__(self, FIRSTNAME, SURNAME, ADDRESS):
        self.FIRSTNAME = FIRSTNAME
        self.SURNAME = SURNAME
        self.ADDRESS = ADDRESS
    
    def register_User(self):
            db.create_all()
            db.session.add(self)
            db.session.commit()
#mysql.connection.
'''class Applicant():
    cur = mysql.connection.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS applicants (FNAME VARCHAR(15), LNAME VARCHAR(155))')
    mysql.connection.commit()
    cur.close()
    '''
    