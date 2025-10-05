
import pytest, allure
from utils.api import post

@allure.feature("Courier")
@allure.story("Login courier")
class TestCourierLogin:
    def test_login_returns_id(self, courier):
        creds = courier["data"]
        r = post("/courier/login", data={"login": creds["login"], "password": creds["password"]})
        assert r.status_code == 200
        assert isinstance(r.json().get("id"), int)

    @pytest.mark.parametrize("miss", ["login", "password"], ids=["no_login","no_password"])
    def test_login_missing_field(self, courier, miss):
        payload = dict(courier["data"])
        payload.pop(miss)
        r = post("/courier/login", data=payload)
        assert r.status_code == 400

    def test_login_wrong_password(self, courier):
        creds = courier["data"]
        r = post("/courier/login", data={"login": creds["login"], "password": "wrong"})
        assert r.status_code in (404, 400)

    def test_login_nonexistent(self):
        r = post("/courier/login", data={"login": "ghost_user", "password": "x"})
        assert r.status_code in (404, 400)
