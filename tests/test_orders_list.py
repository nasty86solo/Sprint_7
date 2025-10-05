
import allure
from utils.api import get

@allure.feature("Orders")
@allure.story("List")
class TestOrdersList:
    def test_list_contains_orders(self):
        r = get("/orders")
        assert r.status_code == 200
        body = r.json()
        assert isinstance(body.get("orders"), list) if isinstance(body, dict) else isinstance(body, list)
