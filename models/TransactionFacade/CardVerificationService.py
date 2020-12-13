from dbController.CardDBController import CardDBController
from models.Result import Result

class CardVerificationService():

    def __init__(self):
        self = self

    def verifyCard(self, cardNum):
        valid = self.validateCardNumber(cardNum)
        if(valid):
            return Result(valid,"Card Verified")
        else:
            return Result(valid,"Card Invalid")
        
    def validateCardNumber(self, cardNum):
        cardDB = CardDBController()
        card = cardDB.getCardByNumber(cardNum)
        if card:
            return True
        else:
            return False
