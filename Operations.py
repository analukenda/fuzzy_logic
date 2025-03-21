from IFuzzySet import IFuzzySet
from IUnaryFunction import IUnaryFunction
from MutableFuzzySet import MutableFuzzySet
from IBinaryFunction import IBinaryFunction

class Operations:
    def unaryOperation(iFuzzySet:IFuzzySet,iUnaryFunction:IUnaryFunction):
        if iFuzzySet is None or iUnaryFunction is None:
            print('Morate zadati set i funkciju!')
            exit(1)
        domain=iFuzzySet.getDomain()
        new_set=MutableFuzzySet(domain)
        for element in domain:
            new_set.set(element,iUnaryFunction.valueAt(iFuzzySet.getValueAt(element)))
        return new_set

    def binaryOperation(iFuzzySet1:IFuzzySet,iFuzzySet2:IFuzzySet,iBinaryFunction:IBinaryFunction):
        if iFuzzySet1 is None or iFuzzySet2 is None or iBinaryFunction is None:
            print('Morate zadati dva seta i funkciju!')
            exit(1)
        domain=iFuzzySet1.getDomain()
        if domain != iFuzzySet2.getDomain():
            print('Setovi moraju biti definirani nad istim domenama!')
            exit(1)
        new_set=MutableFuzzySet(domain)
        for element in domain:
            new_set.set(element,iBinaryFunction.valueAt(iFuzzySet1.getValueAt(element),iFuzzySet2.getValueAt(element)))
        return new_set

    def zadehNot(self):
        iUnaryFunction=IUnaryFunction()
        def zN(x:float):
            return 1-x
        iUnaryFunction.valueAt=zN
        return iUnaryFunction

    def zadehAnd(self):
        iBinaryFunction=IBinaryFunction()
        def zA(x:float,y:float):
            return min(x,y)
        iBinaryFunction.valueAt=zA
        return iBinaryFunction

    def zadehOr(self):
        iBinaryFunction=IBinaryFunction()
        def zO(x:float,y:float):
            return max(x,y)
        iBinaryFunction.valueAt=zO
        return iBinaryFunction

    def hamacherTNorm(v:float):
        if v<0:
            print('V ne moze biti negativan!')
            exit(1)
        iBinaryFunction=IBinaryFunction()
        def hT(x:float,y:float):
            return (x*y)/(v+(1-v)*(x+y-x*y))
        iBinaryFunction.valueAt=hT
        return iBinaryFunction

    def hamacherSNorm(v:float):
        if v<0:
            print('V ne moze biti negativan!')
            exit(1)
        iBinaryFunction=IBinaryFunction()
        def hS(x:float,y:float):
            return (x+y-(2-v)*x*y)/(1-(1-v)*x*y)
        iBinaryFunction.valueAt=hS
        return iBinaryFunction

