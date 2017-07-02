#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


def main():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--location', default='../dataset', help='The location where the Master Dataset should be written. Default: %default.')
    parser.add_option('--sub-folders-details', default='locations,12,sensors,23,devices,10', help='Data details, format <name1>,<size1>,<name2>,<size2>. Default: %default.')

    options, args_left = parser.parse_args()

    # check args
    if options.location is None:
        print 'Missing Masster Data Set target folder.'
        parser.print_help()
        exit(1)
    if options.sub_folders_details is None:
        print 'Missing sub folders details.'
        parser.print_help()
        exit(1)

    # parse sub folders details
    from core import SubFoldersDetailsParser
    parser = SubFoldersDetailsParser()
    sub_folders = parser.process(sub_folders_details=options.sub_folders_details)
    if sub_folders is None:
        print 'Invalid sub folders input config.'
        exit(1)

    # update the master dataset
    from core import MasterDataset
    master_dataset = MasterDataset(path=options.location)
    if not master_dataset.exists():
        print 'Master Dataset (%s) not found !'%(options.location)
        parser.print_help()
        exit(1)

    master_dataset.update(sub_folders)


if __name__ == '__main__':
    main()
