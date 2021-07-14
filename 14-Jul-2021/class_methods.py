class person:
    name="Sai"
    def __init__(self,name,age):
       name=self.name
       print("\n Instance method",name,age)

    @staticmethod
    def sta(rno,id):
        print("\n static method",rno,id)

    @classmethod
    def cla(cls,name,age):
        print("\n Class method",name,age)
        name=cls.name
        print("\n Class method",name,age)

o=person("DEF",10)

o1=person.cla("ABC",12)

o.sta(12345,"Aer234")