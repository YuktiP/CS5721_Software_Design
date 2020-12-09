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