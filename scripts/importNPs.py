#!/usr/bin/env python

"""

    To execute this script run:
                                1) manage.py shell
                                2) exec(open('scripts/importNPs.py').read())
"""
import csv
import os
path =  "scripts/upload" # Set path of new directory here
os.chdir(path) # changes the directory
from planfinder.models import NeighbourhoodPlan, NationalPark, Lpa # imports the model
with open('outputNPsData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['natpark'] == "":
            p = NeighbourhoodPlan(
                plan_name=row['plan_name'],
                plan_url=row['plan_url'],
                lpa=Lpa.objects.get(lpa_name=row['lpa']),
                ref_date=row['ref_date'],
                map_location=row['map_location'],
                #supersededDate=row['supersededDate'],
                created_date=row['created_date'],
                status=row['status'],
                cross_authority_plan=row['cross_authority_plan'],
                )

        else:
            p = NeighbourhoodPlan(
                plan_name=row['plan_name'],
                plan_url=row['plan_url'],
                lpa=Lpa.objects.get(lpa_name=row['lpa']),
                natpark=NationalPark.objects.get(natpark_name=row['natpark']),
                ref_date=row['ref_date'],
                map_location=row['map_location'],
                #supersededDate=row['supersededDate'],
                created_date=row['created_date'],
                status=row['status'],
                cross_authority_plan=row['cross_authority_plan'],
                )
        p.save()
print("complete")

exit()