import logging

logging.basicConfig(level=logging.DEBUG)


class Message(object):

    def __init__(self, text: str = None):
        self.logger = logging.getLogger(type(self).__name__)
        self.text = text
        self.logger.info('Set text value to {}'.format(self.text))

    def __repr__(self):
        return self.text


class Coder(object):

    def _encode(self, message):
        bit_size = 1
        curr_char = 0
        encoded_message = ''
        while curr_char < len(message.text):
            bit = message.text[curr_char:curr_char+bit_size]
            if bit_size % 2 == 1:
                encoded_message += bit
            else:
                encoded_message = bit + encoded_message
            curr_char += bit_size
            bit_size += 1
        message.text = encoded_message

    def _decode(self, message):
        pass

    def transform(self, message: Message, times: int = 0):
        if times:
            action = self._decode if times > 0 else self._encode
            for _ in range(abs(times)):
                action(message)
        return message
