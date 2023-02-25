import unittest

# keeping packages under src requires some kind of path manipulation
# or direct access to the path
# if we were just doing 1 package, and were willing to manipulate the
# package builder then we could make the packages visible at the top
# level. not sure what the best way really is.

from src.example_rg import example


class TestExample(unittest.TestCase):
    def test_string_to_list(self):
        string = "[[1, 2, 3],[4, 5, 6]]"
        my_list = example.string_to_list(string)
        self.assertEqual(my_list, [[1, 2, 3], [4, 5, 6]])


if __name__ == "__main__":
    print(dir(example))
    unittest.main()
