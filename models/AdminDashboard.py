from app import db,app
from Interfaces.IDashboard import IDashboard
from dbController.CardDBController import CardDBController


class AdminDashboard(IDashboard):

    def __init__(self):
        self = self
    
    #def GetDashboardData(self):
     #   self.url = '/registerbatch'
      #  return self
    
    def getAdminDashboardData(self):
        self.template = 'AdminPage.html'
        obj = CardDBController()
        self.cardToBlockList = obj.getBlockRequests()
        self.cardToUnblockList = obj.getUnblockRequests()
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

    

