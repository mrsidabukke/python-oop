# class dan object

class Hero:
# __init__ adalah method constructor

    def __init__(self, name, speed):
            self.name = name
            self.speed = speed
           
# jika ingin mengakses atribut name dari class Hero harus menggunakan parameter    
    def getName(self):      
            return self.name
            
    def getSpeed(self):
            return self.speed
    def getskill(self):
            return 'normal'
    

#inheritance
class JapaneseHero(Hero):
       pass
#        def setAge(self, age):
#             self.age = age
#             return self.age
       
#        def getskill(self):
#             return 'anime'

# # jika class anak memiliki fungsi yang sama dengan yang ada pada parent maka yang akan dijalankan adalah fungsi yang ada pada class anak 
# class IndonesianHero(Hero):
# #cara memanggil fungsi yang ada pada parent
#     def __init__(self, name, speed):
#         super().__init__(name, speed)
#         print('menggunakan fungsi dari parent')


#     def getskill(self):
#         return 'khodam'



# # jika tidak ada maka akan mngikut class parent seperti dibawah ini
# class AmericanHero(Hero):
#     pass       
            

# membuat object hero1
hero = Hero('sniper ', ' slow ')
print(hero.getName() + 'punya speed' + hero.getSpeed())


# jplayer = JapaneseHero('saitama', 'fast')
# print('umur ' + jplayer.getName() + 'adalah ' + jplayer.setAge('25') + 'tahun')

# Iplayer = IndonesianHero('sukarno', 'medium')
# print(Iplayer.getName() + 'memiliki skill ' + Iplayer.getskill())

# Aplayer = AmericanHero('captain america', 'fast')
# print(Aplayer.getName() + 'memiliki skill ' + Aplayer.getskill())