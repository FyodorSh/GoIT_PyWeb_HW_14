from unittest.mock import MagicMock, patch

import pytest
from src.database.models import User

@pytest.fixture()
def test_read_users_me(user):
