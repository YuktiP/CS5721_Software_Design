from app import db

class CustomerApplication(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    firstName=db.Column(db.String(20))
    lastName=db.Column(db.String(20))
    dateOfBirth=db.Column(db.Date)
    address=db.Column(db.String(30))
    city=db.Column(db.String(30))
    pin=db.Column(db.String(10))
    monthly_income=db.Column(db.Integer)
    cardType=db.Column(db.String(20))
    application_type=db.Column(db.String(1))
    occupation=db.Column(db.String(20))
    contact_number=db.Column(db.String(15))
    error_details=db.Column(db.String(40))
    ppsn=db.column(db.Integer)
    email=db.Column(db.String(30))

    def __init__(self,firstName, lastName, dateOfBirth,address,city,pin, monthly_income,cardType, occupation, ppsn,email, contact_number,application_type,  eligibility,error_details):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.monthly_income = monthly_income
        self.application_type = application_type
        self.occupation = occupation
        self.eligibility = eligibility
        self.error_details=error_details
        self.contact_number=contact_number
        self.ppsn = ppsn
        self.city=city
        self.pin=pin
        self.cardType=cardType
        self.email=email
        
    def CollectApplications(self):
        db.create_all()
        db.session.add(self)
        db.session.commit()    