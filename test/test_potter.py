import unittest

from potter.Potter import Potter

class TestPotter(unittest.TestCase):
    def test_add_cart(self):
        p = Potter()
        p.add_cart({"book1": 10, "book2": 1})
        p.add_cart({"book1": 2, "book4": 5})

        result = {"book1": 12, "book2": 1, "book4": 5}

        self.assertDictEqual(p.book_cart, result)
        self.assertDictEqual(p.get_cart(), result)

    def test_simple_price(self):
        p = Potter()
        p.add_cart({"book1": 1})
        self.assertEqual(p.get_price(), 8)

        p = Potter()
        p.add_cart({"book2": 1})
        self.assertEqual(p.get_price(), 8)

        p = Potter()
        p.add_cart({"book3": 1})
        self.assertEqual(p.get_price(), 8)

        p = Potter()
        p.add_cart({"book4": 1})
        self.assertEqual(p.get_price(), 8)

        p = Potter()
        p.add_cart({"book5": 1})
        self.assertEqual(p.get_price(), 8)


if __name__ == "__main__":
    unittest.main()
