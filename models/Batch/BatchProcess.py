from app import db

class BatchProcess(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    batchType=db.Column(db.Integer)
    batchProcessType=db.Column(db.Integer)
    frequency=db.Column(db.String(10))
    date=db.Column(db.Date)
    isActive=db.Column(db.Boolean)
    createdDate=db.Column(db.DateTime)
    createdBy=db.Column(db.Integer)
    lastRunDate=db.Column(db.Date)
    
    def __init__(self,batchType=0,batchTypeName="",batchProcessTypeName="", batchProcessType=0, frequency="",date=None,isActive=False,createdDate=None, createdBy="",lastRunDate=None):
        self.batchType = batchType
        self.batchTypeName = batchTypeName
        self.batchProcessType = batchProcessType
        self.batchProcessTypeName = batchProcessTypeName
        self.frequency = frequency
        self.date = date
        self.isActive = isActive
        self.createdDate = createdDate
        self.createdBy = createdBy
        self.lastRunDate = lastRunDate

    
# Id

# type (Daily, monthly, weekly, fixed, yearly) - Enum

# frequency (Can be 1-7[days of week], 1-30(or 28)[days of month], 1-365[days of year] or null(for daily, fixed) - ArrayField(of ints) - [1, 7] OR [23] OR [235]OR null

# time (time of day in UTC) - ArrayField(of Char strings - ['9:00', '13:30']

# date (for fixed type) - datetime - 2009-03-21

# is_active (boolean) - for enabling, disabling the schedule

# name (CharField) - If you want to name the schedule - batch process type