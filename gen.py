import time
class Bank(): 
    crisis = False
    def create_atm(self, money, moneylimit):
        while not self.crisis:
            if money <= moneylimit:
                yield f"£{money}"
            else:
                yield f"£{money} is not avaible to you, please withdraw a max of £{moneylimit}"
        
        while self.crisis:
            newmoneylimit = 40
            if money <= newmoneylimit:
                yield f"£{money}"
            else:
                if moneylimit >= newmoneylimit:
                    yield f"£{money} is not avaible to you, please withdraw a max of £{newmoneylimit}"
                else:
                    yield f"£{money} is not avaible to you, please withdraw a max of £{moneylimit}"

class user:
    user = {}
    bankrupt = []
    def add_user(self, name, money, account):
        self.user[name] = [money, account]
    def debers(self):
        for name in self.user:
            if self.user[name][0] <= 0:
                self.bankrupt.append(name)
    def interest(self):
        for name in self.user:
            if self.user[name][1] == "Gold":
                self.user[name][0] = (self.user[name][0])*1.08
            elif self.user[name][1] == "Silver":
                self.user[name][0] = (self.user[name][0])*1.06
            elif self.user[name][1] == "Bronze":
                self.user[name][0] = (self.user[name][0])*1.04
            elif self.user[name][1] == "Standard":
                self.user[name][0] = (self.user[name][0])*1.02

user.add_user(True, "John", 900, "Gold")
user.add_user(True, "Mark", 400, "Silver")
user.add_user(True, "Lui", 20, "Standard")
hsbc = Bank() 
for name in user.user:
    y = user.user[name][0]
    corner_street_atm = hsbc.create_atm(400, y)
    print(corner_street_atm.__next__())