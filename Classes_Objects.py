class person:
    name='Ankita'
    age=19
    occupation='AI Engineer'
    def data(self):
        print(f"{self.name} is a {self.occupation}")
a=person()
a.name='Ankita Saini'
b=person()
b.name='Nikita'
b.occupation='Doctor'
c=person()
c.occupation='Python Developer'
# a.occupation='Python Developer'
# print(a.name,a.occupation)
a.data()
b.data()
c.data()