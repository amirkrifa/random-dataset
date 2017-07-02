#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


def main():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--location', default='../dataset', help='The location where the Master Dataset should be written. Default: %default.')
    parser.add_option('--file-size', default=10, help='File size in megabyte. Default: %default.', type=int)
    parser.add_option('--sub-folders-details', default='locations,64,sensors,138,devices,24', help='Data details, format <name1>,<size1>,<name2>,<size2>. Default: %default.')

    options, args_left = parser.parse_args()

    # check args
    if options.location is None:
        print 'Missing Masster Data Set target folder.'
        parser.print_help()
        exit(1)
    if options.file_size is None:
        print 'Missing file size in MB.'
        parser.print_help()
        exit(1)
    if options.sub_folders_details is None:
        print 'Missing sub folders details.'
        parser.print_help()
        exit(1)

    # parse sub folders details
    from core import SubFoldersDetailsParser
    folders_parser = SubFoldersDetailsParser()
    sub_folders = folders_parser.process(sub_folders_details=options.sub_folders_details)
    if sub_folders is None:
        print 'Invalid sub folders input config.'
        exit(1)

    # ensure file size <= sub folders sizes
    invalid_sizes = [x for x in sub_folders if x.size < options.file_size]
    if invalid_sizes:
        print 'invalid_sizes: ', invalid_sizes, [options.file_size]
        print "Invalid input config, found sub folders having a size < file size."
        exit(1)

    # generate the master dataset
    from core import MasterDataset
    master_dataset = MasterDataset(path=options.location)
    if master_dataset.exists():
        print 'Master Dataset (%s) already available !'%(options.location)
        exit(1)
    master_dataset.generate(sub_folders=sub_folders, file_size=options.file_size)

if __name__ == '__main__':
    main()
