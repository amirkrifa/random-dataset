#!/usr/bin/env python

class RandomStringGenerator:
    def __init__(self):
        import string
        self._target_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    def create(self, length):
        """
        Generates a random alpha numeric string of the given length.
        :param length: the length of the string.
        :return: the generated string.
        """
        import random
        return ''.join(random.choice(self._target_chars) for i in range(length))

