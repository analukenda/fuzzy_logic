from Domain import Domain
from MutableFuzzySet import MutableFuzzySet
from DomainElement import DomainElement
import Debug
from CalculatedFuzzySet import CalculatedFuzzySet
from StandardFuzzySets import StandardFuzzySets

d=Domain.intRange(0,11)
set1=MutableFuzzySet(d).set(DomainElement.of(0),1.0).set(DomainElement.of(1),0.8).set(DomainElement.of(2),
                                            0.6).set(DomainElement.of(3),0.4).set(DomainElement.of(4),0.2)
Debug.ispis_2(set1,'Set1:')

d2=Domain.intRange(-5,6)
set2=CalculatedFuzzySet(d2,StandardFuzzySets.lambdaFunction(d2.indexOfElement(DomainElement.of(-4)),
                                                            d2.indexOfElement(DomainElement.of(0)),
                                                            d2.indexOfElement(DomainElement.of(4))))

Debug.ispis_2(set2,'Set2:')
