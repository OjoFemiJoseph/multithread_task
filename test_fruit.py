import unittest
from main import FruitProcessor

class TestFruitProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = FruitProcessor()

    def test_fruit_processing(self):
        self.processor.start()

        while len(self.processor.fruit_tree) > 0 and len(self.processor.dirty_fruit) > 0 and len(self.processor.clean_fruit_lst) < 50:
            pass

        self.assertEqual(len(self.processor.fruit_tree), 0)
        self.assertEqual(len(self.processor.dirty_fruit), 0)
        self.assertEqual(len(self.processor.clean_fruit_lst), 50)

if __name__ == '__main__':
    unittest.main()
