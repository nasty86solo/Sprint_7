
import requests

BASE = "https://qa-scooter.praktikum-services.ru/api/v1"

def post(path, *, json=None, data=None, params=None):
    return requests.post(f"{BASE}{path}", json=json, data=data, params=params, timeout=15)

def get(path, *, params=None):
    return requests.get(f"{BASE}{path}", params=params, timeout=15)

def delete(path):
    return requests.delete(f"{BASE}{path}", timeout=15)
