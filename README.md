# Random Dataset generation, update and backup

****
### Introduction:
The goal of this src code is to be able to:
- generate a random Dataset as a set of files on disk given some input configuration (hierarchy, size ...),
- update an already existing dataset according to some update configuration,
- creating a backup of and existing dataset.

****
### Code structure:
- scripts: the generation, update and backup scripts entry points.
- core: the main classes responsible for random data generation and dataset management.

****
### Running data generation 

```
Usage: generate-dataset.py [options]

Options:
  -h, --help            show this help message and exit
  --location=LOCATION   The location where the Master Dataset should be
                        written. Default: ../dataset.
  --file-size=FILE_SIZE
                        File size in megabyte. Default: 10.
  --sub-folders-details=SUB_FOLDERS_DETAILS
                        Data details, format <name1>,<size1>,<name2>,<size2>.
                        Default: locations,64,sensors,138,devices,24.
```

****
### Running data update

```
Usage: update-dataset.py [options]

Options:
  -h, --help            show this help message and exit
  --location=LOCATION   The location where the Master Dataset should be
                        written. Default: ../dataset.
  --sub-folders-details=SUB_FOLDERS_DETAILS
                        Data details, format <name1>,<size1>,<name2>,<size2>.
                        Default: locations,12,sensors,23,devices,10.

```

****
### Running data backup

```
Usage: backup-dataset.py [options]

Options:
  -h, --help   show this help message and exit
  --src=SRC    The location where the Master Dataset should be written.
               Default: ../dataset.
  --dest=DEST  Backup destination. Default: ../dataset-backup.
```
