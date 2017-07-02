#!/usr/bin/env python

class RandomFileGenerator:
    def __init__(self, min_str_len=100, max_str_len=10000, file_name_seed=1):
        self._max_str_len = max_str_len
        self._min_str_len = min_str_len
        self._file_name_seed = file_name_seed
        self._current_file_id = self._file_name_seed
    def create(self, target_size, target_path):
        """
        Generate a file including random content. The file will be created within the target path.
        :param target_size: the size of the file.
        :param target_path: the target folder path.
        """
        import os
        from random import randint
        from RandomStringGenerator import RandomStringGenerator
        string_generator = RandomStringGenerator()
        f = open(os.path.join(target_path, str(self._current_file_id)), 'w')
        self._current_file_id += 1
        target_size = target_size
        total_size = 0
        while total_size < target_size:
            line_size = min(randint(self._min_str_len, self._max_str_len), target_size - total_size)
            random_str = string_generator.create(line_size)
            f.write('%s\n'%(random_str))
            total_size += len(random_str)
        f.close()

