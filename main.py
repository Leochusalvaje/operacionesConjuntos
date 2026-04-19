class Conjunto:
    def __init__(self,universo,conjuntoA,conjuntoB):
        self.universo=universo
        self.conjuntoA=conjuntoA
        self.conjuntoB=conjuntoB

    def union(self):
        conjunto_union=[]
        for e in self.conjuntoA:
            conjunto_union.append(e)

        for e in self.conjuntoB:
            exito=False
            for e2 in conjunto_union:
                if e == e2:
                    exito=True
                    break
            if exito==False:
                conjunto_union.append(e)
        print(f"La union del conjunto A con el conjunto B es {conjunto_union}")
        return conjunto_union
    
    def interseccion(self,conjuntoA,conjuntoB):
        conjunto_interseccion=[]

        for e1 in conjuntoA:
            for e2 in conjuntoB:
                if(e1==e2):
                    conjunto_interseccion.append(e1)
        if conjunto_interseccion:
            print(f"La interseccion del conjunto A con el conjunto B es {conjunto_interseccion}")
        else:
            print(f"La interseccion del conjunto A con el conjunto B es {conjunto_interseccion} por lo tanto es el conjunto vacío")
        return conjunto_interseccion
    
    def complemento(self,conjunto):
        conjunto_complento=[]
        for e in self.universo:
            exito=False
            for e2 in conjunto:
                if e == e2:
                    exito=True
                    break
            if exito==False:       
                conjunto_complento.append(e)

        print(f"El complemento del conjunto {conjunto} es {conjunto_complento}")
        return conjunto_complento
    
    def diferencia(self,conjuntoA,conjuntoB):
        conjunto_diferencia=[]
        for e in conjuntoA:
            exito=False
            for e2 in conjuntoB:
                if e == e2:
                    exito=True
                    break
            if exito==False:       
                conjunto_diferencia.append(e)

        print(f"La diferencia del conjunto A con el conjunto B es {conjunto_diferencia}")
        return conjunto_diferencia
    
    def diferencia_simetrica(self,conjuntoA,conjuntoB):
        conjunto_diferencia_simetrica=[]
        for e in conjuntoA:
            exito=False
            for e2 in conjuntoB:
                if e == e2:
                    exito=True
                    break
            if exito==False:       
                conjunto_diferencia_simetrica.append(e)
        for e in conjuntoB:
            exito=False
            for e2 in conjuntoA:
                if e == e2:
                    exito=True
                    break
            if exito==False:       
                conjunto_diferencia_simetrica.append(e)

        print(f"La diferencia simétrica del conjunto A con el conjunto B es {conjunto_diferencia_simetrica}")
        return conjunto_diferencia_simetrica


universo = [1,2,3,4,5,6]
A = [1,2]
B = [5,6]

c = Conjunto(universo, A, B)

c.union()
c.interseccion(A, B)
c.complemento(B)
c.diferencia(A, B)
c.diferencia_simetrica(A, B)
