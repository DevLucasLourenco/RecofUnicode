import unicodedata

class RecofUnicode():
    
    def __new__(self, arg):
        self.__adaptado = list()
        return self.run(arg)

    def run(objeto):
        txt_adaptado = ''.join(x for x in unicodedata.normalize('NFD', objeto) if unicodedata.category(x) != 'Mn')
        txt_adaptado = txt_adaptado.replace('ç', 'c')
        return txt_adaptado


if __name__=="__main__":
  texto = RecofUnicode('áãàñç')
  print(texto)
