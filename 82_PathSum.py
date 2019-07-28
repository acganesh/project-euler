import networkx as nx
import csv

test_data = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

def parse():
	my_list= []
	line = 'init'

	with open('82_data.txt', 'rb') as f:
		reader = csv.reader(f)
		for item in reader:
			item_int = [int(x) for x in item]
			my_list.append(item_int)
	return my_list

def main(data):
	length = len(data)
	H = nx.DiGraph()
	H.add_node('S')
	for i in range(length):
		for j in range(length):
			node_id = (i, j)
			if j == 0:
				H.add_edge('S', node_id, weight = data[i][j])
			if 0 <= i-1:
				H.add_edge(node_id, (i-1, j), weight = data[i-1][j])
			if j+1 < length:
				H.add_edge(node_id, (i, j+1), weight=data[i][j+1])
			if i+1 < length:
				H.add_edge(node_id, (i+1, j), weight=data[i+1][j])
			if j+1 == length:
				H.add_edge(node_id, 'E', weight = 0)

	path_length = nx.dijkstra_path_length(H, 'S', 'E')
	path = nx.shortest_path(H, 'S', 'E')
	print path
	return path_length

data = parse()
#print data
print main(data)
print main(test_data)

#Attempted to define graph by using node costs: didn't work with networkX methods.
'''
for i in range(length):
	for j in range(length):
		node_id = str(i)+str(j)
		G.add_node(node_id,weight=data[i][j])
		if 0 <= i-1:
			G.add_edge(node_id, str(i-1)+str(j))
		if j+1 < length:
			G.add_edge(node_id, str(i)+str(j+1))
		if i+1 < length:
			G.add_edge(node_id, str(i+1)+str(j))
'''