class Tmoney:
    def __init__(self, amount = 0):
        self.amount = amount
        self.usd = 28.24
    #-------------------
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, value):
        if value>=0:
            self.__amount = value
        else:
            raise Exception('money amount should be positive!')
    #---------------------
    @property
    def usd(self):
        return self.__usd
    @usd.setter
    def usd(self, value):
        if value<25:
            raise Exception("da ne mozhet byt' takogo")
        else:
            self.__usd = value
            return self.__usd

    #---------------------
    def top_up(self, howmany = 0):
        howmany = float(input('enter how many to + in grn : '))
        self.amount += howmany/self.usd
    def top_down(self, howmany = 0):
        howmany = float(input('enter how many to - in grn : '))
        if self.amount >= howmany:
            self.amount -= howmany/self.usd
        else:
            raise Exception('not enough money!')
    #------------
    def show(self):
        return 'ur balance = {0} , usd = {1}'.format(self.amount , self.usd)
    #------------
    def usd_update(self):
        self.usd = float(input('usd : '))


#--------------------
purse = Tmoney()
purse.top_up()
purse.top_down()
purse.usd_update()
print(purse.show())




