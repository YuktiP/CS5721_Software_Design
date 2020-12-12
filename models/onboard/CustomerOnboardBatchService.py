from models.onboard.CustomerOnboardService import CustomerOnBoardService
import pandas as pd 
from dbController.UserDBController import UserDBController
from models.Result import Result

class CustomerOnBoardBatchService():

    def __init__(self):
        self = self

    def onBoardCustomerBatch(self,docpath):
        data=pd.read_csv(docpath)
        df =pd.DataFrame(data, columns= ['firstName','lastName','dateOfBirth','email','address','city','pin','occupation','monthly_income','cardType','contact_number','ppsn'])
        usersOnboarded = []
        for application in df.itertuples():
            onboardService = CustomerOnBoardService()
            result = onboardService.onBoardCustomer(application)
            usersOnboarded.append(result.data)
        return Result(isSuccess=True,text="Customer Batch Onboarded Successfully", data = usersOnboarded)