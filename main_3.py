from Domain import Domain
from MutableFuzzySet import MutableFuzzySet
from DomainElement import DomainElement
import Debug
from Operations import Operations

d=Domain.intRange(0,11)
set1=MutableFuzzySet(d).set(DomainElement.of(0),1.0).set(DomainElement.of(1),0.8).set(DomainElement.of(2),
                                            0.6).set(DomainElement.of(3),0.4).set(DomainElement.of(4),0.2)
Debug.ispis_2(set1,'Set1:')
notSet1=Operations.unaryOperation(set1,Operations.zadehNot(None))
Debug.ispis_2(notSet1,'notSet1:')
union=Operations.binaryOperation(set1,notSet1,Operations.zadehOr(None))
Debug.ispis_2(union,'Set1 union notSet1:')
hinters=Operations.binaryOperation(set1,notSet1,Operations.hamacherTNorm(1.0))
Debug.ispis_2(hinters,'Set1 intersection with notSet1 using parameterised Hamacher T norm with parameter 1.0:')