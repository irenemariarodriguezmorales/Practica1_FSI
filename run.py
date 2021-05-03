# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
oc = search.GPSProblem('O', 'C'
                       , search.romania)
sd = search.GPSProblem('S', 'D'
                       , search.romania)
tf = search.GPSProblem('T', 'F'
                       , search.romania)
lp = search.GPSProblem('L', 'P'
                       , search.romania)
nm = search.GPSProblem('N', 'M'
                       , search.romania)

print("Ejecuciones con Busqueda en Anchura")
node, count = search.breadth_first_graph_search(ab)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("Ejecuciones con Busqueda en Profundidad")
node, count = search.depth_first_graph_search(ab)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("-----------------------------------------------")
print("Ejecuciones con Nodos A-B")

print("Ramificacion y Acotacion -> ", end='')
node, count = search.ra_graph_search(ab)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("Ramificacion y Acotacion con Subestimacion -> ", end='')
node, count = search.ra_sub_graph_search(ab)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("-----------------------------------------------")
print("Ejecuciones con Nodos O-C")

print("Ramificacion y Acotacion -> ", end='')
node, count = search.ra_graph_search(oc)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("Ramificacion y Acotacion con Subestimacion -> ", end='')
node, count = search.ra_sub_graph_search(oc)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)
print("-----------------------------------------------")
print("Ejecuciones con Nodos S-D")

print("Ramificacion y Acotacion -> ", end='')
node, count = search.ra_graph_search(sd)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("Ramificacion y Acotacion con Subestimacion -> ", end='')
node, count = search.ra_sub_graph_search(sd)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("-----------------------------------------------")
print("Ejecuciones con Nodos T-F")

print("Ramificacion y Acotacion -> ", end='')
node, count = search.ra_graph_search(tf)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("Ramificacion y Acotacion con Subestimacion -> ", end='')
node, count = search.ra_sub_graph_search(tf)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("-----------------------------------------------")
print("Ejecuciones con Nodos L-P")

print("Ramificacion y Acotacion -> ", end='')
node, count = search.ra_graph_search(lp)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("Ramificacion y Acotacion con Subestimacion -> ", end='')
node, count = search.ra_sub_graph_search(lp)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("-----------------------------------------------")
print("Ejecuciones con Nodos N-M")

print("Ramificacion y Acotacion -> ", end='')
node, count = search.ra_graph_search(nm)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

print("Ramificacion y Acotacion con Subestimacion -> ", end='')
node, count = search.ra_sub_graph_search(nm)
print(node.path(), end='')
print(" Nº de nodos visitados: ", end='')
print(count)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
