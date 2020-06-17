#!/usr/bin/env python

"""

    To execute this script run:
                                1) manage.py shell
                                2) exec(open('scripts/lhn/importLocalAuthorities.py').read())
"""
import csv
import os
path =  "lhn/uploads" # Set path of new directory here
os.chdir(path) # changes the directory
from lhn.models import LocalAuthorityLHN, County # imports the model
with open('LHN_Input.csv', encoding='cp1252') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = LocalAuthorityLHN(
            la_code=row['area_code'],
            la_area=row['LA'],
            county=County.objects.get(name=row['County']),
            hp_2018=row['hp_2018'],
            hp_2019=row['hp_2019'],
            hp_2020=row['hp_2020'],
            hp_2021=row['hp_2021'],
            hp_2022=row['hp_2022'],
            hp_2023=row['hp_2023'],
            hp_2024=row['hp_2024'],
            hp_2025=row['hp_2025'],
            hp_2026=row['hp_2026'],
            hp_2027=row['hp_2027'],
            hp_2028=row['hp_2028'],
            hp_2029=row['hp_2029'],
            hp_2030=row['hp_2030'],
            hp_2031=row['hp_2031'],
            hp_2032=row['hp_2032'],
            hp_2033=row['hp_2033'],
            hp_2034=row['hp_2034'],
            hp_2035=row['hp_2035'],
            hp_2036=row['hp_2036'],
            hp_2037=row['hp_2037'],
            hp_2038=row['hp_2038'],
            hp_2039=row['hp_2039'],
            med_aff_rat_2017=row['med_aff_rat_2017'],
            med_aff_rat_2018=row['med_aff_rat_2018'],
            med_aff_rat_2019=row['med_aff_rat_2019'],
            )
        p.save()
print("complete")

exit()