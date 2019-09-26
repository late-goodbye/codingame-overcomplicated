import unittest
from .disordered_first_contact import Message, Coder


class TestMessage(unittest.TestCase):

    def test_text(self):
        test_message = 'test_message'
        message = Message(test_message)
        self.assertEqual(message.text, test_message)
        self.assertEqual(message.__repr__(), test_message)
        self.assertIsNone(Message().text)
        self.assertIsNone(Message().__repr__())


class TestCoder(unittest.TestCase):

    def setUp(self):
        self.coder = Coder()

    def test_encode_message(self):
        message = Message('hello world')
        self.coder.transform(message, -1)
        self.assertEqual(message.text, 'worlelhlo d')

        self.coder.transform(message, -6)
        self.assertEqual(message.text, 'hrlellwo ods')

    def test_decode_message(self):
        pass
