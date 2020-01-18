

from tensortrade.exchanges.services.execution.simulated import execute_order
from tensortrade.exchanges import Exchange
from tensortrade.data import DataFeed, Array


def test_price_ds():

    btc_price = Array("USD/BTC", [7000, 7500, 8300])
    eth_price = Array("USD/ETH", [200, 212, 400])

    feed = DataFeed([btc_price, eth_price])

    assert feed.next() == {"USD/BTC": 7000, "USD/ETH": 200}


def test_exchange_ds():

    btc_price = Array("USD/BTC", [7000, 7500, 8300])
    eth_price = Array("USD/ETH", [200, 212, 400])

    exchange = Exchange("coinbase", service=execute_order)(btc_price, eth_price)

    feed = DataFeed([exchange])
    assert feed.next() == {"coinbase:USD/BTC": 7000, "coinbase:USD/ETH": 200}