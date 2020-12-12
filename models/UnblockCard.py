from app import db,app
from Interfaces.IActionOnCard import IActionOnCard
from dbController.CardDBController import CardDBController
from models.Card import *

class UnblockCard(IActionOnCard):
    
    
    def actionOnCustomerCardList(self):
        self.template = 'UnblockCard.html'
        obj = CardDBController()
        self.cardToUnblockList = obj.getUnblockRequests()
        return self