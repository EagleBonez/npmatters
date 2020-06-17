#!/usr/bin/env python

"""

    To execute this script run:
                                1) manage.py shell
                                2) exec(open('scripts/importCounties.py').read())
"""
import csv
import os
path =  "scripts/upload" # Set path of new directory here
os.chdir(path) # changes the directory
from planfinder.models import County # imports the model
with open('outputCountyData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = County(county_id=row['county_id'], county_name=row['county_name'])
        p.save()
print("complete")

exit()