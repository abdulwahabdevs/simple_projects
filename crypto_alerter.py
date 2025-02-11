from crypto_data import get_coins, Coin
import time

def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, '!!!ALERT TRIGGERED!!!')
            else:
                print(coin)

if __name__ == '__main__':
    coins: list[Coin] = get_coins()

    while True:
        alert('btc', bottom=95_000, top=105_000, coins_list=coins)
        alert('eth', bottom=2_600, top=2_750, coins_list=coins)
        alert('sol', bottom=190, top=210, coins_list=coins)
        print('-'*20) # for lining the difference
        time.sleep(30)