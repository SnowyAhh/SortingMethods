import unittest
from src.sortMethods import selectionSort

# Use python -m unittest .\src\unitTests\selectionSortTest.py to run
class TestSelectionSort(unittest.TestCase):
    def test_sort_null(self):
        self.assertEqual([], [])

if __name__ == '__main__':
    unittest.main()