import unittest
import device


class MyTestCase(unittest.TestCase):
    def test_number_only_handling(self):
        self.assertEqual(device.only_number("1qaz2[]3';.4`5'6vtr7ol-8n,j,9][0"), "1234567890")  # add assertion here


if __name__ == '__main__':
    unittest.main()
