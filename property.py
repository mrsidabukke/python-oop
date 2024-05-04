class Hero:

# __init__ adalah method constructor
    def __init__(self, name, age):
            self.name = name            
            self.age = age

    @property
    # property berfungsi untuk mengubah method menjadi seperti atribut
    def infoPlayer(self):      
            return self.name + ' adalah ' + self.age

    @infoPlayer.setter
    # setter berfungsi untuk merubah nilai atribut property
    def infoPlayer(self, data):      
            # split berfungsi untuk memisahkan data berdasarkan karakter tertentu
            name, age = data.split(' ')
            self.name = name
            self.age = age

          
player = Hero('saitama' , '23')
player.infoPlayer = 'lamhot 25'
# tidak perlu menggunakan tanda kurung karena sudah diubah menjadi atribut
print(player.infoPlayer)
