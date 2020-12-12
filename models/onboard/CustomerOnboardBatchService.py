from models.onboard.CustomerOnboardService import CustomerOnBoardService
import pandas as pd 

class CustomerOnBoardBatchService():

    def __init__(self):
        self = self

    def onBoardCustomerBatch(self,docpath):
        data=pd.read_csv(docpath)
        df =pd.DataFrame(data, columns= ['firstName','lastName','dob','email','address','city','zipcode','occupation','monthlyIncome','cardType'])
        for application in df.itertuples():
            onboardService = CustomerOnBoardService()
            onboardService.onBoardCustomer(application)
        self.result=db.session.query(User).all()
        return self