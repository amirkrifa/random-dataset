#!/usr/bin/env python

import collections
SubFolder = collections.namedtuple('SubFolder', ['name', 'size'])


class SubFoldersDetailsParser:
    def __init__(self, separator=','):
        self._separator = separator
    def _pairwise(self, iterable):
        from itertools import izip
        a = iter(iterable)
        return izip(a, a)
    def process(self, sub_folders_details):
        """
        Parse a sub folder details string.
        :param sub_folders_details: string that describes the sub folders which will be generated.
        :return: list of named tuples. Each named tuple describes a sub folder config.
        """
        sub_folders_details = sub_folders_details.split(self._separator)

        if not sub_folders_details:
            # invalid config
            return None

        if not len(sub_folders_details) % 2 == 0:
            # invalid config
            return None

        sub_folders = []
        for name, size in self._pairwise(sub_folders_details):
            try:
                size = int(size)
            except ValueError:
                print 'Invalid sub folders description'
                return None
            sub_folders.append(SubFolder(name=name, size=size))
        return sub_folders