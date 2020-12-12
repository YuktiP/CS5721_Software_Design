from models.CustomerApplication import CustomerApplication
from app import db

class CustAppDBController():
    def __init__(self):
        self = self

    def addCustomerApplication(self,CustomerApplication):
        db.create_all()
        db.session.add(CustomerApplication)
        db.session.commit()  

    def getApplicationById(self,applicationId):
         application = db.session.query(CustomerApplication).filter(CustomerApplication.id == applicationId).first()
         return application 