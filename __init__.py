import pandas as pd
import unicodedata

class RecofUnicode():
    flag = False
    
    def __new__(self, arg):
        self.texto_tratado: str = ''
        self.lista_tratada: list = list()
        
        if not isinstance(arg, list):    
            self.get(self, arg)
            return self.texto_tratado
        
        else:
            RecofUnicode.flag = True
            self.get(self, arg)
            return self.lista_tratada
        

    def get(self, objeto):
        recof = lambda item: ''.join(x for x in unicodedata.normalize('NFD', item) if unicodedata.category(x) != 'Mn')
        
        if not RecofUnicode.flag:
            self.texto_tratado = recof(objeto)
        else:
            self.lista_tratada = [recof(each) for each in objeto]
            

                    
if __name__=="__main__":
    print(RecofUnicode(['çáãÀâ','ãçâé']))
