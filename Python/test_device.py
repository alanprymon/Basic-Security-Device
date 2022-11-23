import unittest
import device

class MyTestCase(unittest.TestCase):
    def test_number_only_handling(self):
        self.assertEqual(device.only_number("1qaz2[]3';.4`5'6vtr7ol-8n,j,9][0"), "1234567890")  # add assertion here

    def test_unlocking(self):
        check = device.check_unlock("839831", 0, False)
        self.assertTrue(check[1])

    def test_locking(self):
        check = device.check_unlock("839834", 0, True)
        self.assertFalse(check[1])

