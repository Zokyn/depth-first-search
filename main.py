def profundidade(i, n, t, pe, ps, back, parent, v):
    t = t + 1
    
    # print(f'Vertice \t\tv:[{i[v]}]\t\tt:[{t}]')
    pe[v] = t
    back[v] = pe[v]
    # print(f"Vizinhos \t\tN(v):{n[v]}")
    for w in n[v]:
        w = i.index(w)
        if pe[w] == 0:
            # parent[w] = i[v]
            parent[w] = v
            t, pe, ps, back, parent = profundidade(i, n, t, pe, ps, back, parent, w)
            back[v] = min(back[v], back[w])
        elif ps[w] == 0 and parent[v] != w:
            back[v] = min(back[v], pe[w])
    # print(f"{i[v]} saiu da pilha.")
    t = t + 1
    ps[v] = t

    return t, pe, ps, back, parent

def is_articulacao(i, pe, back, parent: list) -> True:
    articulacoes = [False] * len(i)
    for v in range(len(parent)): 
        if parent[v] == None: ### raiz da árvore
            child_count = 0
            for w in parent:
                if w != None and parent[w] == v: child_count = child_count + 1
            if child_count >= 2:
                articulacoes[v] = True # return True
        else:
            child_list = []
            for w in parent:
                if w != None and parent[w] == v:
                    child_list.append(w)
            for w in child_list:
                if(back[w] >= pe[v]):
                    articulacoes[v] = True # return True
    return articulacoes


i = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
n = [
    ['B', 'C', 'D'], 
    ['A', 'D'], 
    ['A', 'B', 'E'], 
    ['A', 'B', 'C'], 
    ['C', 'F', 'G'], 
    ['E', 'G'], 
    ['E', 'F']
    ]
t = 0

pe = [0] * len(i)
ps = [0] * len(i)
back = [0] * len(i)
parent = [None] * len(i)
v = 4
t, pe, ps, back, parent = profundidade(i, n, t, pe, ps, back, parent, v)
print(t, pe, ps, back, parent)
print(i)
print(is_articulacao(i, pe, back, parent))