from IFuzzySet import IFuzzySet
from DomainElement import DomainElement
from Operations import Operations
from MutableFuzzySet import MutableFuzzySet
from Domain import Domain

class Relations:
    def isUTimesURelation(relation:IFuzzySet):
        if IFuzzySet is not None:
            domain=relation.getDomain()
            if domain.getNumberOfComponenst()!=2:
                return False
            if domain.getComponent(0) != domain.getComponent(1):
                return False
            return True
        else:
            print('Mora bit zadan skup!')
            exit(1)

    def isSymmetric(relation:IFuzzySet):
        if relation is not None:
            if Relations.isUTimesURelation(relation):
                domain=relation.getDomain()
                subdomain=domain.getComponent(0)
                cardinality=subdomain.getCardinality()
                for i in range(cardinality-1):
                    element_1=subdomain.elementForIndex(i).getComponentValue(0)
                    for j in range(i+1,cardinality):
                        element_2=subdomain.elementForIndex(j).getComponentValue(0)
                        if relation.getValueAt(DomainElement.of([element_1,element_2])) \
                                != relation.getValueAt(DomainElement.of([element_2,element_1])):
                            return False
                return True
            else:
                return False
        else:
            print('Elemenet domene mora biti zadan!')
            exit(1)

    def isReflexive(relation:IFuzzySet):
        if relation is not None:
            if Relations.isUTimesURelation(relation):
                domain=relation.getDomain()
                subdomain = domain.getComponent(0)
                for i in range(subdomain.getCardinality()):
                    element=subdomain.elementForIndex(i).getComponentValue(0)
                    if relation.getValueAt(DomainElement.of([element,element])) != 1.0:
                        return False
                return True
            else:
                return False
        else:
            print('Set mora bit zadan!')
            exit(1)

    def isMaxMinTransitive(relation:IFuzzySet):
        if relation is not None:
            if Relations.isUTimesURelation(relation):
                domain=relation.getDomain()
                subdomain = domain.getComponent(0)
                cardinality=subdomain.getCardinality()
                for i in range(cardinality):
                    element_1=subdomain.elementForIndex(i).getComponentValue(0)
                    for j in range(cardinality):
                        if i==j:
                            continue
                        element_2=subdomain.elementForIndex(j).getComponentValue(0)
                        for k in range(cardinality):
                            if k==i or k==j:
                                continue
                            element_3=subdomain.elementForIndex(k).getComponentValue(0)
                            if relation.getValueAt(DomainElement.of([element_1,element_3])) >= \
                                Operations.zadehAnd(None).valueAt(relation.getValueAt(DomainElement.of([element_1,element_2])), \
                                                       relation.getValueAt(DomainElement.of([element_2,element_3]))):
                                continue
                            else:
                                return False

                return True

            else:
                return False
        else:
            print('Set mora biti zadan!')
            exit(1)

    def compositionOfBinaryRelations(r1:IFuzzySet,r2:IFuzzySet):
        if r1 is not None and r2 is not None:
            if r1.getDomain().getNumberOfComponenst()==2 and r2.getDomain().getNumberOfComponenst()==2:
                r1_domains=r1.getDomain().getComponent(0),r1.getDomain().getComponent(1)
                r2_domains=r2.getDomain().getComponent(0),r2.getDomain().getComponent(1)
                if r1_domains[1] != r2_domains[0]:
                    print('Relacije moraju imati zajednicke domene!')
                    exit(1)
                composition=MutableFuzzySet(Domain.combine(r1_domains[0],r2_domains[1]))
                domain=composition.getDomain()
                y_domain=r1_domains[1]
                for domain_element in domain:
                    x=domain_element.getComponentValue(0)
                    z=domain_element.getComponentValue(1)
                    outer=[]
                    for y_element in y_domain:
                        y=y_element.getComponentValue(0)
                        xy=r1.getValueAt(DomainElement.of([x,y]))
                        yz=r2.getValueAt(DomainElement.of([y,z]))
                        outer.append(min(xy,yz))
                    composition.set(DomainElement.of([x,z]),max(outer))
                return composition
            else:
                print('Relacije moraju biti binarne!')
                exit(1)
        else:
            print('Relacije moraju biti zadane!')
            exit(1)

    def isFuzzyEquivalence(r:IFuzzySet):
        if r is not None:
            if Relations.isReflexive(r) and Relations.isSymmetric(r) and Relations.isMaxMinTransitive(r):
                return True
            return False
        else:
            print('Relacija mora biti zadana!')
            exit(1)




