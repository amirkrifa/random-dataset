#!/usr/bin/env python

class RandomFolderGenerator:
    def __init__(self, folder_path, folder_name):
        self._folder_name = folder_name
        self._folder_path = folder_path
        import os
        self._absolute_folder_path = os.path.join(self._folder_path, self._folder_name)
    def create(self, target_folder_size, target_file_size):
        """
        Generates a folder of a given size containing files with random contents.
        :param target_folder_size: the folder size.
        :param target_file_size: size of the files which will be included within the sub folders.
        """
        import os
        if not os.path.exists(self._absolute_folder_path):
            os.mkdir(self._absolute_folder_path)
        target_size = target_folder_size
        total_size = 0
        from RandomFileGenerator import RandomFileGenerator
        file_genegrator = RandomFileGenerator()
        while total_size < target_size:
            file_size = min(target_file_size, target_size - total_size)
            file_genegrator.create(file_size, self._absolute_folder_path)
            total_size += file_size
            print '\tcurrent sub folder size (byte): ', total_size

