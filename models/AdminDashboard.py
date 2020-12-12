from app import db,app
from Interfaces.IDashboard import IDashboard
from dbController.CardDBController import CardDBController
from enums.Enums import *

class AdminDashboard(IDashboard):

    def __init__(self, template=None):
        self.template = template
    
    def getDashboardData(self, requestPage):

        if requestPage == "registerbatch":
            return self.dataForBatch()

        self.template = 'AdminPage.html'
        obj = CardDBController()
        self.cardToBlockList = obj.getBlockRequests()
        self.cardToUnblockList = obj.getUnblockRequests()
        return self
    
    def dataForBatch(self):
        self.batchTypes = BatchType.list()
        self.batchProcessTypes = BatchProcessType.list()
        self.template = "ScheduleBatchProcess.html"
        return self

    

    
    #remove them in the last
    #def blockCard(self, cardNumber):
     #   db.session.query(Card).filter(Card.card_number == cardNumber).update({Card.card_status:0})
      #  db.session.commit()
    
    #def unblockCard(self, cardNumber):
    #    db.session.query(Card).filter(Card.card_number == cardNumber).update({Card.card_status:1})
     #   db.session.query(Card).filter(Card.card_number == cardNumber).update({Card.block_request:0})
      #  db.session.commit()
       # return self
    
   # def processBatch(self):
    #    return

    

