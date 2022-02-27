class atm(object):
    def __init__(self, cardnumber, pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def cardnumber(self):
        print("cardnumber")

    def pinnumber(self):
        print("pinnumber")

user1 = car("4796808767981","2500")
user2 = car("6438897564872","2000")
user1.cardnumber()