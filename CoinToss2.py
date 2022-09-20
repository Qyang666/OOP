import CoinClass as c

def show_coin_status(coin_object):
    print("this side of the coin is up:", coin_object.get_sideup()) 

def flip(coin_object):
    coin_object.toss()


my_coin=c.Coin()
print(my_coin.get_sideup())
show_coin_status(my_coin)
