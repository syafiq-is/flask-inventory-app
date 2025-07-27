# Unit Tests

from app import db, Product, Location, ProductMovement


def test_model_relations(app):
    # Ensure we start with empty tables
    assert Product.query.count() == 0
    assert Location.query.count() == 0
    assert ProductMovement.query.count() == 0

    # Create a location and a product
    loc = Location(location_id="WarehouseA")
    prod = Product(product_id="ItemA")
    db.session.add_all([loc, prod])
    db.session.commit()

    # After commit, counts should reflect additions
    assert Product.query.count() == 1
    assert Location.query.count() == 1

    # Create a product movement: moving 5 units to the location
    movement = ProductMovement(
        product_id=prod.product_id,
        qty=5,
        from_location=None,
        to_location=loc.location_id,
    )
    db.session.add(movement)
    db.session.commit()

    # Check that the movement was recorded
    assert ProductMovement.query.count() == 1
    mv = ProductMovement.query.first()
    assert mv.qty == 5
    assert mv.to_location == "WarehouseA"
