# _*_ coding=utf-8 _*_
import unittest
from identity_card import IdentityCard


class TestIDCard(unittest.TestCase):
    _id = IdentityCard("513233199912287676")

    def test_age(self):
        self._id.get_info()
        self.assertEqual(self._id.get_age(), 19)

    def test_generate_id(self):
        id_card = self._id.generate_id_card()
        self.assertTrue(self._id.is_id_card(id_card))

    def test_gender(self):
        self._id.get_info()
        self.assertEqual(self._id.get_gender(), "男")


if __name__ == "__main__":
    unittest.main()
