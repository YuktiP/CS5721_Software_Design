import enum

class ExtendedEnum(enum.Enum):

    @classmethod
    def list(cls):
        l = []
        for i in iter(cls):
            l.append({"Label":i.name,"Selected":False})
        return l

class BatchType(ExtendedEnum):
    Daily = 1
    Monthly = 2 
    Weekly = 3 
    Fixed = 4
    Yearly = 5


class BatchProcessType(ExtendedEnum):
    CalculateInterest = 1
    SettleTransactions = 2
    GenerateStatement = 3
    EmailStatement = 4
    UpdateReportingDB = 5

class Role(ExtendedEnum):
    Admin = 1
    Employee = 2
    Customer = 3

class Status(ExtendedEnum):
    Active = 1
    Inactive = 0

class CardType(ExtendedEnum):
    Basic = 1
    Black = 2
    Student = 3

class TransactionType(ExtendedEnum):
    Debit = 1
    Credit = 2
    Authorization = 3
    Reversal = 4
    InterestCalculation = 5

class SourceType(ExtendedEnum):
    POS = 1
    ATM = 2
    Ecommerce = 3
    BankNetwork = 4
    System = 5