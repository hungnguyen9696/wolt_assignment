import unittest
import requests

class Test_API(unittest.TestCase):
    def test_check_status_code_equals_200(self):
        data= {
            "cart_value": 1500,
            "delivery_distance": 5000,
            "number_of_items": 8,
            "time": "2022-01-29T16:00:00Z"
        }
        response = requests.post("http://127.0.0.1:8000/fee", json=data)
        self.assertEqual(response.status_code, 200)

    def test_delivery_fee(self):
        data = {
            "cart_value": 1500,
            "delivery_distance": 4000,
            "number_of_items": 8,
            "time": "2022-01-29T16:00:00Z"
        }
        response = requests.post("http://127.0.0.1:8000/fee", json=data)
        self.assertEqual(response.json()["delivery_fee"], 1000)

    def test_delivery_fee_onFriday(self):
        data = {
            "cart_value": 1500,
            "delivery_distance": 4000,
            "number_of_items": 8,
            "time": "2022-01-28T16:00:00Z"
        }
        response = requests.post("http://127.0.0.1:8000/fee", json=data)
        self.assertEqual(response.json()["delivery_fee"], 1100)

    def test_delivery_fee_withlessthan500mdistance(self):
        data = {
            "cart_value": 1000,
            "delivery_distance": 499,
            "number_of_items": 8,
            "time": "2022-01-29T16:00:00Z"
        }
        response = requests.post("http://127.0.0.1:8000/fee", json=data)
        self.assertEqual(response.json()["delivery_fee"], 300)

    def test_delivery_fee_with_cartvalue_surcharge(self):
        data = {
            "cart_value": 500,
            "delivery_distance": 499,
            "number_of_items": 8,
            "time": "2022-01-29T16:00:00Z"
        }
        response = requests.post("http://127.0.0.1:8000/fee", json=data)
        self.assertEqual(response.json()["delivery_fee"], 800)

if __name__ == '__main__':
    unittest.main()