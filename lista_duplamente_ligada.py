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

class ListaLigada:
    def __init__(self):
        self.__inicio = None
        self.__final = None

     def append(self, aluno: Aluno):
        if self.__inicio == None:
            self.__inicio = aluno
            self.__final = aluno
            
        else:
            if self.__final.ante == None:              
              self.__final.ante = self.__inicio
              self.__final.prox = aluno
              aluno.ante = self.__final
              self.__final = aluno
              
            else:
              self.__final.ante = self.__final.prox
              self.__final.prox = aluno
              aluno.ante = self.__final
              self.__final = aluno



    def pop(self):
        atual = self.__inicio

        if atual == None:
            raise EmptyLinkedList

        if atual.prox == None:
            self.__final = None
            self.__inicio = None
            return atual

        while atual.prox != self.__final:
            atual = atual.prox
        atual.prox = None
        retorno = self.__final
        self.__final = atual
        return retorno

    def __repr__(self):
        saida = ''
        atual = self.__inicio
        while atual != None: 
            saida += f'{atual}'
            atual = atual.prox
            if atual != None:
                saida += ' -> '
        return f'[{saida}]'

lista = ListaLigada()
lista.append(Aluno('A1', 9.8))
lista.append(Aluno('A2', 7.8))
lista.append(Aluno('A3', 9.8) )
lista.append(Aluno('A4', 8.8) )
print(lista)    


