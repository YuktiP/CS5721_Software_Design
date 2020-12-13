from app import db,app
from Interfaces.IDashboard import IDashboard
from dbController.CardDBController import CardDBController
from models.BlockCard import BlockCard
from models.UnblockCard import UnblockCard
from enums.Enums import *

class AdminDashboard(IDashboard):

    def __init__(self, template=None):
        self.template = template
    
    def getDashboardData(self, requestPage):

        if requestPage == "registerbatch":
            return self.dataForBatch()
        elif requestPage == "showrequests":
            return self.dataForCardRequests()
        elif requestPage == "block":
            return self.blockCardRequests()
        elif requestPage == "unblock":
            return self.unblockCardRequests()
        
    
    def dataForBatch(self):
        self.batchTypes = BatchType.list()
        self.batchProcessTypes = BatchProcessType.list()
        self.template = "ScheduleBatchProcess.html"
        return self

    def dataForCardRequests(self):
        self.template = 'AdminPage.html'
        obj = CardDBController()
        self.cardToBlockList = obj.getBlockRequests()
        self.cardToUnblockList = obj.getUnblockRequests()
        return self

    def blockCardRequests(self):
        self.template = 'BlockCard.html'
        blockCard = BlockCard()
        self.blockCardRequests = blockCard.actionOnCustomerCardList()
        return self

    def unblockCardRequests(self):
        self.template = 'UnblockCard.html'
        unblockCard = UnblockCard()
        self.unblockCardRequests = unblockCard.actionOnCustomerCardList()
        return self

    
    
    

