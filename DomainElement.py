class DomainElement:
    def __init__(self, values):
        if values is None:
            print('Morate zadati element domene!')
            exit(1)
        try:
            self.values=[]
            for value in values:
                self.values.append(int(value))
        except TypeError:
            print('Element domene mora bit zadan kao lista elemenata!')
            exit(1)
        except ValueError:
            print('Elementi domene moraju biti cijeli brojevi!')
            exit(1)

    def getNumberOfComponents(self):
        return len(self.values)

    def getComponentValue(self,index:int):
        if index<0 or index>=self.getNumberOfComponents():
            print('Ne postoji element na tom indeksu!')
            return None
        return self.values[index]

    def __eq__(self, o):
        if o is not None:
            if o.__class__ == self.__class__:
                if o.values == self.values:
                    return True
        return False

    def __str__(self):
        if self.getNumberOfComponents()==1:
            return str(self.values[0])
        s='('
        for value in self.values[:-1]:
            s+=str(value)+', '
        return s+str(self.values[-1])+')'

    def of(tuple):
        if tuple is None:
            print('Element domene ne moze biti None!')
            exit(1)
        int_elements=[]
        try:
            for element in tuple:
                int_elements.append(int(element))
        except TypeError:
            try:
                int_elements.append(int(tuple))
            except ValueError:
                print('Elementi domene mogu biti samo cijeli brojevi!')
                exit(1)
        except ValueError:
            print('Elementi domene mogu biti samo cijeli brojevi!')
            exit(1)
        return DomainElement(int_elements)

    def __iter__(self):
        return iter(self.values)




