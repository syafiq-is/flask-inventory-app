import pytest
import os, sys

# Add project root to sys.path so 'import app' works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app as flask_app, db, Product, Location, ProductMovement


@pytest.fixture(scope="function")
def app():
    """
    Provide a fresh Flask app and in-memory database for each test.
    """
    # Configure testing environment
    flask_app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    )
    with flask_app.app_context():
        # Create tables
        db.create_all()
        yield flask_app
        # Teardown: drop tables and cleanup
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="function")
def client(app):
    """
    Return a Flask test client using the app fixture.
    """
    return app.test_client()
