import unittest
from solutions import valid_palindrome, two_sum, reverse_str, is_anagram_dict

class TestSolutions(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(valid_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(valid_palindrome("race a car"))
        self.assertTrue(valid_palindrome(" "))
        self.assertFalse(valid_palindrome("0P"))

    def test_two_sum(self):
        self.assertTrue(two_sum([2, 7, 11, 15], 9) == [0, 1])
        self.assertTrue(two_sum([3, 2, 4], 6) == [1, 2])
        self.assertTrue(two_sum([3, 3], 6) == [0, 1])
        self.assertTrue(two_sum([1, 2, 3], 7) == [])

    def test_reverse_str(self):
        self.assertTrue(reverse_str("hello")=="olleh")
        self.assertTrue(reverse_str("python") == "nohtyp")
        self.assertTrue(reverse_str("a")=="a")
        self.assertTrue(reverse_str("") =="")
        self.assertTrue(reverse_str("OP") == "PO")
        
    def test_is_anagram_dict(self):
        self.assertTrue(is_anagram_dict("banana", "abanan"))
        self.assertFalse(is_anagram_dict("CAR", "JAR"))
        self.assertTrue(is_anagram_dict("anagram", "nagaram"))
        self.assertFalse(is_anagram_dict("CAR", "nagaram"))

    

if __name__ == "__main__":
    unittest.main()