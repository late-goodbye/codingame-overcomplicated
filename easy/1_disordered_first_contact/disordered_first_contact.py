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

    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

    def encode(self, message):
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
        self.logger.info('Encoded message "{}" to "{}"'.format(message, encoded_message))
        message.text = encoded_message

    def decode(self, message):
        decoded_message = ''
        self.logger.info('Decoded message "{}" to "{}"'.format(message, decoded_message))

    def transform(self, message: Message, times: int = 0):
        self.logger.info('Started transforming message "{}"'.format(message))
        if times:
            action = self.decode if times > 0 else self.encode
            self.logger.info('Chose action "{}"'.format(action.__name__))
            for i in range(abs(times)):
                self.logger.info('Started iteration {}'.format(i))
                action(message)
                self.logger.info('Finished iteration {}'.format(i))
        self.logger.info('Finished transformation')
        self.logger.info('Result: "{}"\n'.format(message))
        return message
