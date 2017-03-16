import unittest

from pydux import create_store

from badgecheck import verify
from badgecheck.reducers import main_reducer
from badgecheck.store import INITIAL_STATE


class InitializationTests(unittest.TestCase):
    def test_store_initialization(self):
        def no_op(state, action):
            return state
        store = create_store(no_op, INITIAL_STATE)
        self.assertEqual(store.get_state(), INITIAL_STATE)

    def test_verify_function(self):
        url = 'https://example.org/beths-robotics-badge.json'
        results = verify(url)
        self.assertEqual(results.get('input').get('url'), url)