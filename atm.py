class atm:
    def __init__(self,name,cardnumber,pinnumber):
        self.name=name
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def setColor(self,cardnumber):
        print("This cards number is "+self.cardnumber)

mynum=atm("mynum", 130, 123)
mynum.pinnumber("123")