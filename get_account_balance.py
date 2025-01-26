# Run this code to check if your api key and api secrets are connected correctly. If you see your account balance, it means the api is working.
#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)
# Add your Binance API keys here
key = 'Your_api_key'
secret = 'Your_api_secret'

um_futures_client = UMFutures(key=key, secret=secret)

try:
    response = um_futures_client.balance(recvWindow=6000)
    #logging.info(response)  #Shows the balance of all coins in the account
    for asset in response:
        if asset['asset'] == 'USDT':
            usdt_balance = asset['balance']
            print(f"USDT Balance: {usdt_balance}")
            break
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
