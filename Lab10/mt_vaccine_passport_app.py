"""
Name: {Supisara Kongthong}
SID: {364211760017}
Group: {MIT221}
"""

from model import Person,Student,Vaccine,Vaccine_Passport

p1 = Person("Supisara",22,45.0,151)

v1 = Vaccine("Astazeneca")
d1 = "20/10/2564"


vp1 = Vaccine_Passport(p1)

vp1.vaccine_passport_info()

vp1.add_vaccine(v1)
vp1.add_date(d1)

vp1.vaccine_passport_info()

v2 = Vaccine("Sinovac")
d2 = "21/11/2564"

vp1.add_vaccine(v2)
vp1.add_date(d2)
vp1.vaccine_passport_info()

s1 = Student("Jeno",22,65.00,180,"MIT")

v3 = Vaccine("Pfizer")
d3 = "28/7/2654"

vp2 = Vaccine_Passport(s1)
vp2.add_vaccine(v3)
vp2.add_date(d3)
vp2.vaccine_passport_info()