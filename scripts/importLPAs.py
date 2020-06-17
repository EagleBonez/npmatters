#!/usr/bin/env python

"""

    To execute this script run:
                                1) manage.py shell
                                2) exec(open('scripts/importLPAs.py').read())
"""
import csv
import os
path =  "scripts/upload" # Set path of new directory here
os.chdir(path) # changes the directory
from planfinder.models import Lpa, County # imports the model
with open('outputLPAdata.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Lpa(
            lpa_id=row['lpa_id'],
            lpa_name=row['lpa_name'],
            county=County.objects.get(county_name=row['county']),
            LAD19CD=row['LAD19CD'],
            LAD19NM=row['LAD19NM'],
            )
        p.save()
print("complete")

exit()