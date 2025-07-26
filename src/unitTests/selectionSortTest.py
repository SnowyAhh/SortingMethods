import unittest
from src.sortMethods import selectionSort

# Use python -m unittest .\src\unitTests\selectionSortTest.py to run
class TestSelectionSort(unittest.TestCase):
    # Test for arrays holding non-integers (testing util file)
    def test_non_int(self):
        self.assertEqual(selectionSort.sort(['a', False, 'b']), 
                                            ['a', False, 'b'])

    # Test for arrays holding non-integers and integers (testing util file)
    def test_non_int_and_int(self):
        self.assertEqual(selectionSort.sort([1,'a',False,'b']), 
                                            [1,'a',False,'b'])
        self.assertEqual(selectionSort.sort(['a',False,1,'b']), 
                                            ['a',False,1,'b'])

    # Tests for selection sort
    # Test for empty array
    def test_sort_null(self):
        self.assertEqual(selectionSort.sort([]), [])

    # Test for array with single element
    def test_sort_single(self):
        self.assertEqual(selectionSort.sort([0]), [0])
        self.assertEqual(selectionSort.sort([-100]), [-100])

    # Test for array with multiple elements (no dupes)
    def test_sort_no_dupes(self):
        self.assertEqual(selectionSort.sort([1,3,4,2,5]), [1,2,3,4,5])
        self.assertEqual(selectionSort.sort([-10,54,20,4,6111,-53,0,12]), 
                                            [-53,-10,0,4,12,20,54,6111])
        self.assertEqual(selectionSort.sort([5,4,3,2,1]), [1,2,3,4,5])
        self.assertEqual(selectionSort.sort([-1,-2,-3,-4,-5]), [-5,-4,-3,-2,-1])
        self.assertEqual(selectionSort.sort([1,3]), [1,3])

    # Test for array with duplicate elements
    def test_sort_dupes(self):
        self.assertEqual(selectionSort.sort([1,1,1]), [1,1,1])
        self.assertEqual(selectionSort.sort([1,2,2,1]), [1,1,2,2])
        self.assertEqual(selectionSort.sort([5,3,1,5,-2,-6,5]), 
                                            [-6,-2,1,3,5,5,5])