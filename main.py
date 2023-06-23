def profundidade(i, n, t, pe, ps, back, parent, v):
    t = t + 1
    
    print(f'Vertice \t\tv:[{i[v]}]\t\tt:[{t}]')
    pe[v] = t
    back[v] = pe[v]
    print(f"Vizinhos \t\tN(v):{n[v]}")
    for w in n[v]:
        w = i.index(w)
        if pe[w] == 0:
            parent[w] = i[v]
            t, pe, ps, back, parent = profundidade(i, n, t, pe, ps, back, parent, w)
            back[v] = min(back[v], back[w])
        elif ps[w] == 0 and parent[v] != w:
            back[v] = min(back[v], pe[w])
    print(f"{i[v]} saiu da pilha.")
    t = t + 1
    ps[v] = t

    return t, pe, ps, back, parent
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

print(profundidade(i, n, t, pe, ps, back, parent, v))