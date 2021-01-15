import random
class company:
    def __init__(self,price):
        self.share_price = price
        self.ret = 0
    def buy(self,qty):
        self.share_price += 0.00005*self.share_price
    def sell(self,qty):
        self.share_price -= 0.00005*self.share_price
    def trade(self,cost,misc,sell):
        self.ret = sell - (cost + misc)
        if(ret<0):
            # people shall sell shares if company has negative performance
            # you have to connect this with time 
        return ret

        
msft = company(100)
for i in range(1000):
    if(random.random() < 0.3):
        msft.sell(0)
    else:
        msft.buy(0)
print(msft.share_price)