#!/usr/bin/env python


class MasterDataset:
    def __init__(self, path):
        self._path = path

    def exists(self):
        """
        Check if a dataset exists.
        """
        import os
        return os.path.exists(self._path)

    def _update_sub_folder(self, sub_folder_name, additional_size):
        """
        Updates an existing sub folder according the given additional size.
        :param sub_folder_name: sub folder name.
        :param additional_size: the additional size to add to the sub folder.
        """
        import os
        files = sorted([f for f in os.listdir(os.path.join(self._path, sub_folder_name)) if os.path.isfile(os.path.join(self._path, sub_folder_name, f))])
        file_update_chunk  = additional_size / len(files)
        total_added_size = 0
        from RandomStringGenerator import RandomStringGenerator
        string_generator = RandomStringGenerator()

        while total_added_size < additional_size:
            print '\n'
            for file in files:
                print '\tUpdating file: ', '/'.join([sub_folder_name, file]), ', Current subfolder total added size: ', total_added_size, ', Target additional size: ', additional_size
                if total_added_size > additional_size:
                    break
                string_size = min(file_update_chunk, additional_size - total_added_size)
                str = string_generator.create(string_size)
                f = open(os.path.join(self._path, sub_folder_name, file), 'a')
                f.write('%s\n'%(str))
                f.close()
                total_added_size += string_size

    def generate(self, sub_folders, file_size):
        """
        Generates the master dataset.
        :param sub_folders: the sub folders configuration.
        :param file_size: size of the files which will be generated within the sub folders.
        """
        import os
        os.mkdir(self._path)
        from RandomFolderGenerator import RandomFolderGenerator
        print 'Target subfolders config: ', sub_folders
        print 'Target file size (MB): ', file_size
        for sub_folder in sub_folders:
            print '\nGenerating sub folder: ', sub_folder
            folder_generator = RandomFolderGenerator(folder_path=self._path, folder_name=sub_folder.name)
            folder_generator.create(target_file_size=file_size*1000000, target_folder_size=sub_folder.size*1000000)

    def update(self, sub_folders):
        """
        Updates an existing Master Dataset given the sub folders update configuration.
        :param sub_folders: sub folders update configuration.
        """
        import os
        for sub_folder in sub_folders:
            if not os.path.exists(os.path.join(self._path, sub_folder.name)):
                print 'Invalid existing dataset. Unable to find (%s) sub folder !'%(sub_folder.name)
                exit(1)
            print '\nUpdating subfolder: ', sub_folder.name, ', target additional size: ', sub_folder.size, ' MB'
            self._update_sub_folder(sub_folder.name, sub_folder.size*1000000)


    def backup(self, dest_dataset_path):
        """
        Creates a backup of an existing Master dataset towards the given destination.
        :param dest_dataset_path: backup destination path.
        """
        import os
        # create the dest backup folder if does not exist
        if not os.path.exists(dest_dataset_path):
            os.mkdir(dest_dataset_path)

        sub_folders = [f for f in os.listdir(self._path) if os.path.isdir(os.path.join(self._path, f))]
        for sub_folder_name in sub_folders:
            files = sorted([f for f in os.listdir(os.path.join(self._path, sub_folder_name)) if os.path.isfile(os.path.join(self._path, sub_folder_name, f))])
            for file_name in files:
                source_file = os.path.join(self._path, sub_folder_name, file_name)
                destination_sub_folder = os.path.join(dest_dataset_path, sub_folder_name)
                if not os.path.exists(destination_sub_folder):
                    os.mkdir(destination_sub_folder)
                destination_file = os.path.join(destination_sub_folder, file_name)
                if os.path.exists(destination_file):
                    source_stat = os.stat(source_file)
                    dest_stat = os.stat(destination_file)
                    if source_stat.st_mtime <= dest_stat.st_mtime:
                        print 'Skipping up-to-date file: ', destination_file
                        continue

                print 'Copying file: ', source_file
                # copy line by line without loading the whole file in memory
                with open(destination_file, 'w') as dest_f:
                    with open(source_file, 'r') as source_f:
                        for line in source_f:
                            dest_f.write(line)
        print 'Done'

