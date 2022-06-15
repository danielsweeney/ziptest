
from zipfile import ZipFile
import os

file_name = "go1.17.3.windows-amd64.zip"

with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done')
