#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


def main():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--src', default='../dataset', help='The location where the Master Dataset should be written. Default: %default.')
    parser.add_option('--dest', default='../dataset-backup', help='Backup destination. Default: %default.')

    options, args_left = parser.parse_args()

    if options.src is None:
        print 'Missing source path !'
        parser.print_help()
        exit(1)

    if options.dest is None:
        print 'Missing dest path !'
        parser.print_help()
        exit(1)

    from core import MasterDataset
    master_dataset = MasterDataset(path=options.src)

    if not master_dataset.exists():
        print 'Unable to find src dataset !'
        parser.print_help()
        exit(1)

    master_dataset.backup(dest_dataset_path=options.dest)

if __name__ == '__main__':
    main()
