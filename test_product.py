import pytest
from product import Product

def test_create_normal_product():
    product = Product("Example Product", 10.99, 5)
    assert product.name == "Example Product"
    assert product.price == 10.99
    assert product.quantity == 5
    assert product.active is True

def test_create_product_with_invalid_details():
    with pytest.raises(Exception):
        Product("", -5.99, 10)

def test_product_becomes_inactive_at_0_quantity():
    product = Product("Example Product", 10.99, 0)
    assert product.active is False

def test_product_purchase_modifies_quantity_and_returns_right_output():
    product = Product("Example Product", 10.99, 5)
    purchase_quantity = 3
    output = product.purchase(purchase_quantity)
    assert product.quantity == 2
    assert output == f"You purchased {purchase_quantity} units of Example Product."

def test_buying_larger_quantity_than_exists_invokes_exception():
    product = Product("Example Product", 10.99, 5)
    with pytest.raises(Exception):
        product.purchase(10)

