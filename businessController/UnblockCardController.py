from dbController.CardDBController import CardDBController


class UnblockCardController():

    def __init__(self):
        self = self


    def initiateUnblockCard(self, cardNumber):
        self.cardNumber = cardNumber
        dbObj = CardDBController()
        dbObj.setCardUnblockStatus(cardNumber)
