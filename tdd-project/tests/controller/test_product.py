
from typing import List
from tests.factories import product_data
from fastapi import status
import pytest

async def test_usecases_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())
    
    content = response.json()
    del content['created_at']
    del content['update_at']
    del content['id']
    
    assert response.status_code == status.HTTP_201_CREATED
    assert content == {'name': 'Iphone 15 Pro Max', 'quantity': 10, 'price': '10.500', 'status': True}
    
async def test_usecases_get_should_return_success(client, products_url, product_inserted):
    response = await client.post(f"{products_url}{product_inserted.id}")

    content = response.json()
    del content['created_at']
    del content['update_at']
    
    assert response.status_code == status.HTTP_200_OK
    assert content == {'id': str(product_inserted.id), 'name': 'Iphone 15 Pro Max', 'quantity': 10, 'price': '10.500', 'status': True}
    
async def test_usecases_get_should_return_not_found(client, products_url):
    response = await client.post(f"{products_url}bfee9f62-4b43-48c0-8132-49a75a400e3d")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Product not found with filter: bfee9f62-4b43-48c0-8132-49a75a400e3d"}

@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_success(client, products_url):
    response = await client.get(products_url)
    
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1
    
async def test_usecases_patch_should_return_success(client, products_url, product_inserted):
    response = await client.patch(f"{products_url}{product_inserted.id}", json={"price": "9.800"})

    content = response.json()
    del content['created_at']
    del content['update_at']

    assert response.status_code == status.HTTP_200_OK
    assert content == {'id': str(product_inserted.id), 'name': 'Iphone 15 Pro Max', 'quantity': 10, 'price': '9.800', 'status': True}
    
async def test_usecases_delete_should_return_success(client, products_url, product_inserted):
    response = await client.delete(f"{products_url}{product_inserted.id}")
    
    assert response.status_code == status.HTTP_204_NO_CONTENT

async def test_usecases_delete_should_return_not_found(client, products_url):
    response = await client.delete(f"{products_url}bfee9f62-4b43-48c0-8132-49a75a400e3d")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Product not found with filter: bfee9f62-4b43-48c0-8132-49a75a400e3d"}
