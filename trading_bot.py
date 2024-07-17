import requests
class TradingBot:
    def __init__(self, api_key, access_token):
        self.api_key = api_key
        self.access_token = access_token
        self.base_url = "https://api-v2.upstox.com/"

    def place_order(self, symbol, transaction_type, quantity):
        url = self.base_url + "order/place"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        payload = {
            'variety': 'regular',
            'tradingsymbol': symbol,
            'symbol_token': 'your_symbol_token',
            'transaction_type': transaction_type,
            'quantity': quantity,
            'order_type': 'market',
            'product': 'delivery'
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get('order_id')
        else:
            print(f"Error placing order: {response.text}")
            return None

    def modify_order(self, order_id, quantity):
        try:
            order = self.upstox.modify_order(
                order_id=order_id,
                quantity=quantity
            )
            return order
        except Exception as e:
            print(f"Error modifying order: {e}")
            return None

    def cancel_order(self, order_id):
        try:
            order = self.upstox.cancel_order(order_id)
            return order
        except Exception as e:
            print(f"Error canceling order: {e}")
            return None

    def get_order_details(self, order_id):
        try:
            order_details = self.upstox.get_order_details(order_id)
            return order_details
        except Exception as e:
            print(f"Error fetching order details: {e}")
            return None

    def get_order_history(self):
        try:
            order_history = self.upstox.get_order_history()
            return order_history
        except Exception as e:
            print(f"Error fetching order history: {e}")
            return None

    def get_order_book(self):
        try:
            order_book = self.upstox.get_order_book()
            return order_book
        except Exception as e:
            print(f"Error fetching order book: {e}")
            return None

    def get_trades(self):
        try:
            trades = self.upstox.get_trades()
            return trades
        except Exception as e:
            print(f"Error fetching trades: {e}")
            return None

    def get_order_trades(self, order_id):
        try:
            order_trades = self.upstox.get_order_trades(order_id)
            return order_trades
        except Exception as e:
            print(f"Error fetching order trades: {e}")
            return None

    def get_trade_history(self):
        try:
            trade_history = self.upstox.get_trade_history()
            return trade_history
        except Exception as e:
            print(f"Error fetching trade history: {e}")
            return None
