from fastapi import status
import pytest
from src.main import books

BASE_URL = '/books'


def test_get_all_books(test_client):
    response = test_client.get(f"{BASE_URL}/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == len(books)


@pytest.mark.parametrize("status_filter", ["Private"])
def test_get_all_private_books(test_client, status_filter):
    response = test_client.get(f"{BASE_URL}/?status={status_filter}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


@pytest.mark.xfail
def test_invalid_statuses(test_client):
    response = test_client.get(f"{BASE_URL}/", params={"status": "Unknow"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


def test_non_string_characters(test_client):
    response = test_client.post(
        BASE_URL,
        json={'id': 1, 'author': 3, "decription": 'Good Book'}
    )
    assert response.status_code == 422


def test_valid_id(test_client):
    response = test_client.get(
        BASE_URL, params={"id": 1}
    )
    assert response.status_code == 200


def test_valid_id_delete(test_client):
    response = test_client.delete('/books/1')
    assert response.status_code == 200


def test_valid_id_update(test_client):
    num = 1
    response = test_client.put(
        f"{BASE_URL}/{num}",
        json={
            "id": num,
            "author": "Aut",
            "description": "interesting book",
            "year": 2005
        }
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
    assert response.status_code == 200
    assert response.json()["author"] == "Aut"


def test_invalid_id_add(test_client):
    num = 1
    response = test_client.post(
        f"{BASE_URL}/{num}",
        json={
            "id": num,
            "author": "Aut",
            "description": "interesting book",
            "year": 2005
        }
    )
    assert response.status_code == 405


def test_valid_addition(test_client):
    num = 20
    response = test_client.post(
        f"{BASE_URL}/{num}",
        json={
            "id": num,
            "author": "Aut",
            "description": "interesting book",
            "year": 2005
        }
    )
    assert response.status_code == 405


def test_invalid_id_delete(test_client):
    response = test_client.delete('/books/19')
    assert response.status_code == 404
