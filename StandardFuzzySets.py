from IIntUnaryFunction import IIntUnaryFunction

class StandardFuzzySets:
    def lFunction(alpha:int,beta:int):
        def l(x:int):
            if x<alpha:
                return 1
            if x>=beta:
                return 0
            return (beta-x)/(beta-alpha)
        iIntUnaryFunction=IIntUnaryFunction()
        iIntUnaryFunction.valueAt=l
        return iIntUnaryFunction

    def gammaFunction(alpha:int,beta:int):
        def gamma(x:int):
            if x<alpha:
                return 0
            if x>=beta:
                return 1
            return (x-alpha)/(beta-alpha)
        iIntUnaryFunction=IIntUnaryFunction()
        iIntUnaryFunction.valueAt=gamma
        return iIntUnaryFunction

    def lambdaFunction(alpha:int,beta:int,gama:int):
        def lambd(x:int):
            if x<alpha:
                return 0
            if x>=alpha and x<beta:
                return (x-alpha)/(beta-alpha)
            if x>=gama:
                return 0
            return (gama-x)/(gama-beta)
        iIntUnaryFunction=IIntUnaryFunction()
        iIntUnaryFunction.valueAt=lambd
        return iIntUnaryFunction


