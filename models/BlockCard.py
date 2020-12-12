from app import db,app
from Interfaces.IActionOnCard import IActionOnCard
from dbController.CardDBController import CardDBController
from models.Card import *

class BlockCard(IActionOnCard):
    
    
    def actionOnCustomerCardList(self):
        obj = CardDBController()
        self.cardToBlockList = obj.getBlockRequests()
        return self