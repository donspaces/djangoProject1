import datetime

from django.test import TestCase
from django.utils import timezone
from Module.models import *

# Create your tests here.
class test:
    def sample_saving(self):
        TableI.objects.all().delete()
        hana = TableI(name="Hana", birth="2008-3-7", height=142.3)
        hinata = TableI(name="Hinata", birth="2008-5-10", height=140.7)
        noa = TableI(name="Noa", birth="2007-11-24", height=141.7)
        koyori = TableI(name="Koyori", birth="2008-2-20", height=138.6)
        kanon = TableI(name="Kanon", birth="2008-2-28", height=141.0)
        hana.save()
        hinata.save()
        noa.save()
        koyori.save()
        kanon.save()
        print(TableI.objects.all())

    def filtering(self):
        result = TableI.objects.filter(height__gt = 140.0).order_by("name")
        for i in result: print((i.name, i.birth, i.height))

    def update(self):
        noa = TableI.objects.get(name="Noa")
        noa.height = 142.7
        noa.save()
        print(TableI.objects.all())

    def truncate(self):
        TableI.objects.all().delete()
        print(TableI.objects.all())

def test_db():
    try:
        TestI = test()
        TestI.sample_saving()
        TestI.filtering()
        TestI.update()
        TestI.filtering()
        TestI.truncate()
    except Exception as e:
        print(e.args)
