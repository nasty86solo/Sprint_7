
import pytest, allure
from utils.api import post
from utils.generator import order as gen_order

@allure.feature("Orders")
@allure.story("Create")
class TestOrdersCreate:
    @pytest.mark.parametrize("colors", [
        pytest.param(["BLACK"], id="black"),
        pytest.param(["GREY"], id="grey"),
        pytest.param(["BLACK","GREY"], id="both"),
        pytest.param([], id="no_color"),
    ])
    def test_create_order(self, colors, created_order):
        body = gen_order(colors=colors)
        r = post("/orders", json=body)
        assert r.status_code == 201
        track = r.json().get("track")
        assert isinstance(track, int)
        created_order.append(track)
