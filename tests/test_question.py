import datetime
from decimal import Decimal
import sys
import os
import requests
from unittest.mock import MagicMock, patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from data.question import (
    create_view_completed_orders,
    create_view_electronics_products,
    total_spending_per_customer,
    order_details_with_total,
    find_invalid_emails,
    find_null_or_empty_emails,
    extract_lastname_from_fullname,
    concat_name_and_email,
    cast_price_to_integer,
    find_customers_not_example_email
)

# Eğer fonksiyonlar bir modül içindeyse importu düzeltirsin buddy (örneğin your_module_name = db_functions gibi)

def test_create_view_completed_orders():
    result = create_view_completed_orders()
    assert result is None  # CREATE VIEW komutu bir şey döndürmez

def test_create_view_electronics_products():
    result = create_view_electronics_products()
    assert result is None  # CREATE VIEW komutu bir şey döndürmez

def test_total_spending_per_customer():
    result = total_spending_per_customer()
    assert result is not None
    assert isinstance(result, list)

def test_order_details_with_total():
    result = order_details_with_total()
    assert result is not None
    assert isinstance(result, list)

def test_find_invalid_emails():
    result = find_invalid_emails()
    assert result is not None
    assert isinstance(result, list)

def test_find_null_or_empty_emails():
    result = find_null_or_empty_emails()
    assert result is not None
    assert isinstance(result, list)

def test_extract_lastname_from_fullname():
    result = extract_lastname_from_fullname()
    assert result is not None
    assert isinstance(result, list)
    if result:
        assert 'last_name' in result[0] or isinstance(result[0], tuple)  # Tuple veya dict olabilir

def test_concat_name_and_email():
    result = concat_name_and_email()
    assert result is not None
    assert isinstance(result, list)

def test_cast_price_to_integer():
    result = cast_price_to_integer()
    assert result is not None
    assert isinstance(result, list)

def test_find_customers_not_example_email():
    result = find_customers_not_example_email()
    assert result is not None
    assert isinstance(result, list)

def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # hata varsa exception fırlatır
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")


class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1

def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")
    
    user_score = (collector.passed / (collector.passed + collector.failed)) * 100
    print(round(user_score, 2))
    
    url = "https://edugen-backend-487d2168bc6c.herokuapp.com/projectLog/"
    payload = {
        "user_id": 34,
        "project_id": 4,
        "user_score": round(user_score, 2),
        "is_auto": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    send_post_request(url, payload, headers)

if __name__ == "__main__":
    run_tests()