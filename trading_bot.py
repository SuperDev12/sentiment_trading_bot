import requests
import logging

# Initialize logging
logging.basicConfig(filename='logs/trading_bot.log', level=logging.INFO)

class TradingBot:
    def __init__(self, api_key, api_secret, redirect_uri, access_token):
        self.api_key = api_key
        self.api_secret = api_secret
        self.redirect_uri = redirect_uri
        self.access_token = access_token
        self.base_url = "https://api.upstox.com/v2"
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }

    def place_order(self, symbol, action, quantity):
        url = f"{self.base_url}/order/place"
        payload = {
            "transaction_type": "B" if action == "BUY" else "S",
            "symbol": symbol,
            "quantity": quantity,
            "order_type": "MKT",
            "product": "I"
        }

        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response_data = response.json()
            if response.status_code == 200:
                order_id = response_data.get("order_id")
                logging.info(f"Order placed successfully: {order_id}")
                return order_id
            else:
                logging.error(f"Error placing order: {response_data}")
                return None
        except Exception as e:
            logging.error(f"Error placing order: {str(e)}")
            return None

    def modify_order(self, order_id, quantity=None, price=None):
        url = f"{self.base_url}/order/modify"
        payload = {
            "order_id": order_id,
            "quantity": quantity,
            "price": price
        }
        
        try:
            response = requests.put(url, headers=self.headers, json=payload)
            return response.json()
        except Exception as e:
            logging.error(f"Error modifying order: {str(e)}")
            return None

    def cancel_order(self, order_id):
        url = f"{self.base_url}/order/cancel"
        payload = {
            "order_id": order_id
        }
        
        try:
            response = requests.delete(url, headers=self.headers, json=payload)
            return response.json()
        except Exception as e:
            logging.error(f"Error canceling order: {str(e)}")
            return None

    def get_order_details(self, order_id):
        url = f"{self.base_url}/order/details"
        payload = {
            "order_id": order_id
        }
        
        try:
            response = requests.get(url, headers=self.headers, json=payload)
            return response.json()
        except Exception as e:
            logging.error(f"Error getting order details: {str(e)}")
            return None

    def get_order_history(self):
        url = f"{self.base_url}/order/history"
        
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()
        except Exception as e:
            logging.error(f"Error getting order history: {str(e)}")
            return None

    def get_order_book(self):
        url = f"{self.base_url}/order/retrieve-all"
        
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()
        except Exception as e:
            logging.error(f"Error getting order book: {str(e)}")
            return None

    def get_trades(self):
        url = f"{self.base_url}/order/trades/get-trades-for-day"
        
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()
        except Exception as e:
            logging.error(f"Error getting trades: {str(e)}")
            return None

    def get_order_trades(self, order_id):
        url = f"{self.base_url}/order/trades"
        payload = {
            "order_id": order_id
        }
        
        try:
            response = requests.get(url, headers=self.headers, json=payload)
            return response.json()
        except Exception as e:
            logging.error(f"Error getting order trades: {str(e)}")
            return None

    def get_trade_history(self):
        url = f"{self.base_url}/charges/historical-trades"
        
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()
        except Exception as e:
            logging.error(f"Error getting trade history: {str(e)}")
            return None
