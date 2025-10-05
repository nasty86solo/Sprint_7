
import pytest, allure
from utils.api import post
from utils.generator import courier as gen_courier

@allure.feature("Courier")
@allure.story("Create courier")
class TestCourierCreate:
    def test_courier_can_be_created(self):
        body = gen_courier()
        r = post("/courier", data=body)
        assert r.status_code == 201
        assert r.json().get("ok") is True

    def test_cannot_create_same_twice(self):
        body = gen_courier(login="same_login")
        assert post("/courier", data=body).status_code in (201, 409)
        r = post("/courier", data=body)
        assert r.status_code in (409, 400)

    @pytest.mark.parametrize("key", ["login", "password", "firstName"], ids=["no_login","no_password","no_firstName"])
    def test_required_fields(self, key):
        body = gen_courier()
        body.pop(key)
        r = post("/courier", data=body)
        assert r.status_code == 400
