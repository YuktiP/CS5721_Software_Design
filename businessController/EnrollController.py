from models.CustomerApplication import CustomerApplication  
from dbController.CustAppDBController import CustAppDBController
class EnrollController():

    def enrollForCard(self,form):
        application = self.getCustomerDetails(form)
        self.saveCustomerApplication(application)
        

    def getCustomerDetails(self,form):

        cust=CustomerApplication()
        cust.firstName = form.first_name.data
        cust.lastName = form.last_name.data
        cust.dateOfBirth = form.date_of_birth.data
        cust.address = form.address.data
        cust.monthly_income = form.monthly_income.data
        cust.application_type = 'O'
        cust.occupation = form.occupation.data
        cust.contact_number=form.contact_number.data
        cust.ppsn = form.ppsn.data
        cust.city=form.city.data
        cust.zipcode=form.zipcode.data
        cust.cardType=form.cardType.data
        cust.email=form.email.data
        cust.eligibility = 1
        
        return cust

    def saveCustomerApplication(self,cust):
        appDB = CustAppDBController()
        appDB.addCustomerApplication(cust)


        