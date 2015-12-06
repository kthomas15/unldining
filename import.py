#YOU NEED THESE TO IMPORT DATA

import os, sys, string, csv, datetime, time, django

# This line imports your settings. You need to change fooproject to the name of your project

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dining.settings")

from django.conf import settings

#You need to change the next line to your app.models and import the name of the models in there.

from dininghall.models import Hall, Meals

from django.template.defaultfilters import slugify, urlize

django.setup()

reader = csv.reader(open("dininghall2.csv", "rU"), dialect=csv.excel)

for row in reader:
    if row[0] != "":
        if row[0] == "DATE":
            pass
        else:
            dateparseexample = time.strptime(row[0], "%m/%d/%y")
            dateexample = datetime.datetime(dateparseexample.tm_year, dateparseexample.tm_mon, dateparseexample.tm_mday)
            dhall = row[1].title()
            dhallslug = slugify(row[1])
            dh, dhcreated = Hall.objects.get_or_create(name=dhall, name_slug=dhallslug)
            if row[2] != "":
                bre = int(row[2])
            else:
                bre = None
            if row[3] != "":
                lun = int(row[3])
            else:
                lun = None
            if row[4] != "":
                din = int(row[4])
            else:
                din = None
            if row[5] != "":
                lat = int(row[5])
            else:
                lat = None
            if row[6] != "":
                tot = int(row[6])
            else:
                tot = None
            meal, mealcreated = Meals.objects.get_or_create(meal_date=dateexample, hall=dh, breakfast=bre, lunch=lun, dinner=din, late_night=lat, total=tot)
            print meal
    else:
        pass