#!/usr/bin/env python

"""

    To execute this script run:
                                1) manage.py shell
                                2) exec(open('scripts/lhn/importCounties.py').read())
"""
import csv
import os
path =  "lhn/uploads" # Set path of new directory here
os.chdir(path) # changes the directory
from lhn.models import County # imports the model
with open('County.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = County(name=row['County'])
        p.save()
print("complete")

exit()