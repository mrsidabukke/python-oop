class Hero:
    job = 'hero'
# __init__ adalah method constructor

    def __init__(self, name):
            self.name = name
            #private variabel
            # self._age = 23
            #protected variabel
            self.__age = '23'

# jika ingin mengakses atribut name dari class Hero harus menggunakan parameter    
    def getName(self):      
            return self.name
    def getAge(self):
            return self.__age

#class method && static method
#static method tidak bisa mengakses variabel yang ada pada class
    @staticmethod
    def retiredIn(age):
        return str (40-age) 

#class method bisa mengakses variabel yang ada pada class    
# tapi tidak bisa mengakses object yang ada pada class
    @classmethod
    def generalInfo(cls, age):
        return cls.job + ' akan pensiun dalam ' + cls.retiredIn(age) + ' tahun'
          
          


# player = Hero('saitama')
# print(player.getAge())
print(Hero.retiredIn(23))
print(Hero.generalInfo(30))