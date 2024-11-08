wallet = 25
socks = 0

for price in range(10):
    if wallet >= price:
        wallet = wallet - price
        socks = socks + 1
    else:
        break
        
if ( socks % 2 == 0 ):   # fill in this condition 
    print("I can pair my socks")
else:
    print("I need one more ...")