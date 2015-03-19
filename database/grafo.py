# -*- coding: latin -*-
'''
Classe Grafo
A ser utilizada por db para determinar quais tabelas devem
  ser ligadas para se gerar um comando sql
'''

class Grafo:
    
    def __init__(self):
        self.lista = {}
        '''
        Lista é um dicionário que compõe a lista de adjacências,
          sendo a entrada o nome do elemento e o valor uma lista
          contendo os elementos aos quais esse faz "fronteira"
          no formato de uma tupla (aresta, peso)
        '''
    
    def __str__(self):
        return str(self.lista)
        
        
    def addElemento(self, elemento, vizinhos, pesos = None, valor = None,
            vizinhos2 = None, pesos2 = None, valor2 = None):
        '''
        elemento é o identificador do elemento (string ou numero)
        vizinhos é uma lista com os elementos vizinhos deste
            elemento -> vizinho
        pesos é uma lista com os pesos de cada aresta representada
            em vizinhos
            por padrão todos os valores são 1
        valor é uma lista com o valor associado a cada aresta
            diferente do peso, como se fosse um nome da aresta
        vizinhos2 é uma lista com os elementos que esté é vizinho
            vizinho -> elemento
            por padrão é o mesmo valor de vizinhos (grafo não direcionado)
        pesos2 é uma lista com os pesos de cada aresta representada
            em vizinhos2
            por padrão todos os valores são 1
        valor2 é uma lista com o valor associado a cada aresta
            diferente do peso, como se fosse um nome da aresta
        '''
        if pesos == None:
            pesos = []
            for _ in vizinhos:
                pesos.append(1)
            pesos = tuple(pesos)
            
        if valor == None:
            valor = []
            for _ in vizinhos:
                valor.append(None)
            valor = tuple(valor)
        
        self.lista[elemento] = [ (vizinhos[i], pesos[i], valor[i]) for i in range(len(vizinhos)) ]
        
        if vizinhos2 == None:
            vizinhos2 = vizinhos
            
        if pesos2 == None:
            pesos2 = []
            for i in vizinhos2:
                pesos2.append(1)
            pesos2 = tuple(pesos2)
            
        if valor2 == None:
            valor2 = []
            for _ in vizinhos:
                valor2.append(None)
            valor2 = tuple(valor)
        
        for i in range(len(vizinhos2)):
            if vizinhos2[i] not in self.lista.keys():
                self.lista[ vizinhos2[i] ] = []
            if (elemento, pesos2[i]) not in self.lista[ vizinhos2[i] ]:
                self.lista[ vizinhos2[i] ].append( (elemento, pesos2[i], valor2[i]) )
        
    def buscaLargura(self, raiz):
        '''
        realiza busca em largura no grafo a partir do elemento raiz
        retorna um dicionário com as distâncias de raiz até o elemento
            e um dicionário com o elemento "pai" de cada um
            esse elemento pai é através de quem se chega ao elemento
        '''
        fila = []
        cor = {}
        dist = {}
        pai = {}
        
        for i, _ in self.lista.iteritems():
            cor[i] = 'b'
            dist[i] = None
            pai[i] = None
            
        cor[raiz] = 'c'
        dist[raiz] = 0
        
        fila.append(raiz)
        
        while fila != []:
            u = fila.pop(0)
            for (v,p,_) in self.lista[u]:
                if cor[v] == 'b':
                    cor[v] = 'c'
                    dist[v] = dist[u] + p
                    pai[v] = u
                    fila.append(v)
                    
        return dist, pai
      
    def caminho(self, elementos):
        '''
        define um caminho que percorre todos os elementos
            busca minimizar o caminho, mas não garante que
            será sempre o caminho mínimo
        elementos é uma lista com o nome de todos os elementos
            que devem ser percorridos
        retorna uma lista com tuplas relacionando (origem, destino)
        '''
        dist = {}
        pai = {}
        
        for i in elementos:
            dist[i], pai[i] = self.buscaLargura(i)
            dist[i] = sum([x for a, x in dist[i].iteritems() if a in elementos])
        [(i, _)] = filter(lambda x: x == min(dist.items(), key=lambda x: x[1]), dist.items())
        #pai[i] tem o caminho "ótimo"
        
        ret = []
        for e in elementos:
            res = self.__caminhaArvore(pai[i], e)
            for j in range(len(res)-1):
                campo = ''
                for k in self.lista[res[j]]:
                    if k[2] in [x[2] for x in self.lista[res[j+1]]]:
                        campo = k[2]
                if campo != None:
                    ret.append((('%s.%s')%(res[j], campo), ('%s.%s')%(res[j+1], campo)))
                else:
                    ret.append((('%s')%res[j], ('%s')%res[j+1]))
        
        return ret
        
        
    def __caminhaArvore(self, pai, elemento):
        '''
        pai é um dicionário contendo o pai de cada elemento na arvore
        elemento é o elemento no qual se inicia a caminhada
        Retorna o caminho feito na arvore do epailemento até a raiz
        '''
        if pai[elemento] == None:
            return [elemento]
        else:
            return self.__caminhaArvore(pai, pai[elemento]) + [elemento]
        
        
    
if __name__ == "__main__":
    g = Grafo()
    
    g.addElemento('A', ['C', 'I'], valor=['ac', 'ai'])
    g.addElemento('C', ['A', 'I', 'L', 'M'], valor=['ca', 'ci', 'cl', 'cm'])
    g.addElemento('M', ['C', 'L'], valor=['mc', 'ml'])
    g.addElemento('L', ['M', 'C', 'I'], valor=['lm', 'lc', 'li'])
    g.addElemento('I', ['L', 'C', 'A', 'D'], valor=['il', 'ic', 'ia', 'id'])
    g.addElemento('D', ['I'], valor=['di'])
    
    print g.caminho(['A', 'L', 'M'])