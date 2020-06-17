#!/usr/bin/env python

"""

    To execute this script run:
                                1) manage.py shell
                                2) exec(open('scripts/importNatParks.py').read())
"""
import csv
import os
path =  "scripts/upload" # Set path of new directory here
os.chdir(path) # changes the directory
from planfinder.models import NationalPark # imports the model
with open('outputNatParkData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = NationalPark(natpark_id=row['natpark_id'], natpark_name=row['natpark_name'])
        p.save()

exit()