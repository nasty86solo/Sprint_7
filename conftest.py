
import pytest, allure
from utils.api import post, delete
from utils.generator import courier as build_courier

@pytest.fixture(scope="function")
def courier():
    data = build_courier()
    with allure.step("Создаём курьера"):
        r = post("/courier", data=data)
        assert r.status_code in (201, 409), f"unexpected status {r.status_code}: {r.text}"
    with allure.step("Логинимся и получаем id"):
        lr = post("/courier/login", data={"login": data["login"], "password": data["password"]})
        cid = lr.json().get("id")
    yield {"data": data, "id": cid}
    if cid:
        with allure.step(f"Удаляем курьера {cid}"):
            delete(f"/courier/{cid}")

@pytest.fixture
def created_order():
    tracks = []
    yield tracks
    for t in tracks:
        with allure.step(f"Отменяем заказ {t}"):
            post("/orders/cancel", json={"track": t})
