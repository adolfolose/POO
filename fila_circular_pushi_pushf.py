class EmptyLinkedList(Exception):
    def __init__(self):
        super().__init__('Lista vazia')


class Aluno:
    def __init__(self, nome: str, nota: float):
        self.__nome = nome
        self.__nota = nota
        self.__prox = None
        self.__ante = None

    def __repr__(self):
        return f'{self.__nome}:{self.__nota}'

    @property
    def prox(self):
        return self.__prox
    
    @prox.setter
    def prox(self, prox):
        self.__prox = prox

    @property
    def ante(self):
        return self.__ante
    
    @ante.setter
    def ante(self, ante):
        self.__ante = ante

class ListaCircular:
    def __init__(self):
        self.__inicio = None
        self.__final = None

    def appendi(self, aluno: Aluno):
        
        if self.__inicio == None:
            aluno.prox = aluno
            aluno.ante = aluno
            self.__inicio = aluno
            self.__final = aluno
            print(aluno, aluno.ante, aluno.prox)
            
        else:
            if self.__inicio == self.__final:
              aluno.prox = self.__inicio
              aluno.ante = self.__inicio
              self.__inicio = aluno
              self.__final.prox=aluno
              print(aluno, aluno.ante, aluno.prox)


            else:    
              aluno.prox = self.__inicio
              aluno.ante = self.__final 
              self.__final.prox = aluno
              self.__inicio.ante = aluno
              self.__inicio = aluno
              print(aluno, aluno.ante, aluno.prox, self.__inicio.ante, self.__inicio.prox)
    
    
    def appendf(self, aluno: Aluno):
        
        if self.__inicio == None:
            aluno.prox = aluno
            aluno.ante = aluno
            self.__inicio = aluno
            self.__final = aluno
            print(aluno, aluno.ante, aluno.prox)
            
        else:
            if self.__inicio == self.__final:
              aluno.prox = self.__inicio
              aluno.ante = self.__inicio
              self.__final = aluno
              self.__inicio.prox=aluno
              print(aluno, aluno.ante, aluno.prox)


            else:    
              aluno.prox = self.__inicio
              aluno.ante = self.__final 
              self.__final.prox = aluno
              self.__final = aluno
              self.__inicio.ante = aluno
              print(aluno, aluno.ante, aluno.prox, self.__inicio.ante, self.__inicio.prox)
            
    def pop(self, valor):
        aux1 = 1
        atual = self.__inicio

        if atual == None:
            raise EmptyLinkedList

        while aux1 < valor:
            aux1 +=1
            atual = atual.prox

        if aux1 == valor:
            if atual == self.__inicio:
                self.__inicio = self.__inicio.prox
                
            aux = atual.ante
            aux.prox = atual.prox
            aux = atual.prox
            aux.ante = atual.ante
            return atual

    def __repr__(self, ):
        saida = ''
        atual = self.__inicio

        while ((atual.prox != self.__inicio) ): 
            saida += f'{atual}'
            atual = atual.prox
            if atual.prox != self.__inicio.prox and atual != self.__inicio:
                saida += ' -> '
        saida += f'{atual}'
        return f'[{saida}]'

lista = ListaCircular()
lista.appendi(Aluno('A1', 9.8))
lista.appendi(Aluno('A2', 7.8))
lista.appendf(Aluno('A3', 9.8) )
lista.appendf(Aluno('A4', 8.8) )
lista.appendf(Aluno('A5', 8.8) )
lista.appendf(Aluno('A6', 8.8) )
lista.appendi(Aluno('A7', 8.8) )
lista.appendi(Aluno('A8', 8.8) )
lista.appendi(Aluno('A9', 8.8) )
lista.pop()
print(lista)    