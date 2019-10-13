import logging
from math import floor, sqrt

logging.basicConfig(level=logging.DEBUG)


class Message(object):

    def __init__(self, text: str = None):
        self.logger = logging.getLogger(type(self).__name__)
        self.text = text
        self.logger.info('Set text value to {}'.format(self.text))

    def __repr__(self):
        return self.text

    def __len__(self):
        return len(self.text)


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
        """
        Decodes message once.

        The first step is to determine how many bits the message contains and lengths of the bits.
        The bits lengths in common are 1, 2, 3, ..., k, k + 1, ... .
        We know only the message's total length, it equals 1 + 2 + 3 + ... + k + k'
        k' is one of the next values: [0..k+1].
        Sum of all bits except the last one is 1 + 2 + 3 + ... + k = (1 + k) / 2 * (n - 1) = l.
        Total length is L = l + k', hence k' = L - l.

        L is already known.
        n - 1 = k => (1 + k) / 2 * k = l
        k^2 + k - 2l = 0

        if k' = 0 then L = l, n = k
        if k' = k + 1 then L = l, n = k + 1

        Let's find k for these cases:

        k^2 + k - 2L = 0
        D = 1 + 8L
        k = (-1 + sqrt(1 + 8L)) / 2

        So if k is not integer we have to found floor(k)
        """
        decoded_message = ''
        self.logger.info('Started decoding message {}'.format(message))
        bits_num = floor((-1 + sqrt(1 + 8 * len(message))) / 2)
        expected_message_length = int((1 + bits_num) / 2 * bits_num)
        self.logger.info('The message contains at least {} bits'.format(bits_num))
        last_bit_length = len(message) - expected_message_length or 0

        head = bits_num % 2 == 0
        if last_bit_length:
            self.logger.info('The message has shortened last bit with length {}'.format(last_bit_length))
            head = not head
        bit_size = bits_num

        def cut_message(message, head, bit_size):
            if head:
                bit, message.text = message.text[:bit_size], message.text[bit_size:]
            else:
                message.text, bit = message.text[:-bit_size], message.text[-bit_size:]
            return bit

        while len(message) > 0:
            self.logger.info('Message length is {}'.format(len(message)))
            if last_bit_length:
                bit = cut_message(message, head, last_bit_length)
                last_bit_length = 0
            else:
                bit = cut_message(message, head, bit_size)
                bit_size -= 1

            decoded_message = '{}{}'.format(bit, decoded_message)
            head = not head

        self.logger.info('Decoded message to "{}"'.format(decoded_message))
        message.text = decoded_message

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


if __name__ == '__main__':
    n = int(input())
    message = Message(input())
    coder = Coder()
    print(coder.transform(message, n))
