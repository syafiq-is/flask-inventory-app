from app import db, Product, Location, ProductMovement


# Integration Tests
def test_home_page(client):
    # Home shows Products and Locations sections
    res = client.get("/")
    assert res.status_code == 200
    assert b"Products" in res.data
    assert b"Locations" in res.data


def test_add_product(client):
    # Add a product via POST to index and verify it's listed
    res = client.post("/", data={"product_name": "TestProduct"}, follow_redirects=True)
    assert res.status_code == 200
    assert b"TestProduct" in res.data


def test_add_location(client):
    # Add a location via POST to index and verify it's listed
    res = client.post(
        "/", data={"location_name": "TestLocation"}, follow_redirects=True
    )
    assert res.status_code == 200
    assert b"TestLocation" in res.data


def test_movements_page(client):
    # Movements page loads correctly, follow redirect for trailing slash
    res = client.get("/movements/", follow_redirects=True)
    assert res.status_code == 200
    # Check for table header or known label
    assert b"Qty" in res.data or b"Quantity" in res.data
