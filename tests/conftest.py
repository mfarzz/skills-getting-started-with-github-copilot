from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app


@pytest.fixture
def client():
    original_activities = deepcopy(app.activities)

    with TestClient(app.app) as test_client:
        yield test_client

    app.activities.clear()
    app.activities.update(original_activities)
