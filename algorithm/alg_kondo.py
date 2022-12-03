from heapq import heappop, heappush

class CRIST:
    
    def fit(self, n: int, dist: list[list[int]]) -> list[int]:
        
        self.dist = dist
        self.n = n

        route = self.ans()
        return route

    def ans(self):

        mst = self.prim() #minimum spanning tree
        degree = self.degree(mst) #degree of each node
        sub = self.sub_graph(degree) #graph of odd-degree-nodes
        matching = self.match(sub, degree) #minimum matching
        euler_graph = self.unite(mst, matching) #sub + matching has euler circuit
        euler_circuit = self.circuit(euler_graph, degree) #make circuit
        hamilton = self.skip(euler_circuit) #make trail

        return hamilton[1]


    def ans2(self):
        mst = self.prim()
        tmp = mst
        for i in range(len(tmp)):
            mst.append( (tmp[i][0], (tmp[i][1][1], tmp[i][1][0])) )
        degree = self.degree(mst)
        circuit = self.circuit(mst, degree)
        weight, hamilton_path = self.skip(circuit)

        return hamilton_path

    def ans3(self):#directed
        mst = self.prim()
        degree = self.directed_degree(mst)
        sub = self.directed_sub_graph(degree)
        matching = self.directed_match(sub, degree)
        euler_graph = self.unite(mst, matching)
        euler_circuit = self.directed_circuit(euler_graph, degree)
        weight, hamilton_path = self.skip(euler_circuit)

        return  hamilton_path

    def prim(self):
        tree = [] #answer
        heap = [] #heap
        marked = [False for _ in range(self.n)] #marked?
        new_node = 0 #new node marked lately
        marked[new_node] = True #marked first node
        count = 1 #the number of marked node
        weight = 0 #total weight
        while count < self.n:
            for i in range(self.n):
                if marked[i] == True: #skip
                    continue
                heappush(heap, (self.dist[new_node][i], (new_node, i))) #push all neighbor of current tree

            for i in heap:
                line = heappop(heap) #check whether addable to tree
                if marked[line[1][1]] == False:
                    break
            
            #new_vertex
            weight += line[0]
            marked[line[1][1]] = True
            count += 1
            new_node = line[1][1]
            tree.append(line)

        tree.sort()
        return tree
    
    def degree(self, mst):
        deg = [0 for _ in range(self.n)]
        for i in range(len(mst)):
            deg[mst[i][1][0]] += 1
            deg[mst[i][1][1]] += 1

        return deg
    
    def sub_graph(self, deg):
        sub = []
        for i in range(self.n):
            for j in range(i, self.n):
                if deg[i] % 2 == 0 or deg[j] % 2 == 0 or i == j:
                    continue
                sub.append( (self.dist[i][j], (i, j)) )

        sub.sort()
        return sub
    
    def match(self, sub, deg):
        matching = []
        for e in sub:
            if deg[e[1][0]] % 2 == 1 and deg[e[1][1]] % 2 == 1:
                matching.append(e)
                deg[e[1][0]] += 1
                deg[e[1][1]] += 1

        return matching

    def unite(self, mst, matching):
        euler = mst
        euler.extend(matching)
        euler.sort()

        return euler

    def circuit(self, euler_graph, deg):
        ans = []
        stack = []
        list = euler_graph
        current_node = list[0][1][0]

        while deg[current_node]>0 or stack != []:
            if deg[current_node] == 0:
                ans.append(current_node)
                current_node = stack.pop()
            else:
                stack.append(current_node)
                for neighbor in list:
                    if neighbor[1][0] == current_node:
                        deg[current_node] -= 1
                        deg[neighbor[1][1]] -= 1
                        current_node = neighbor[1][1]
                        list.remove(neighbor)
                        break
                    elif neighbor[1][1] == current_node:
                        deg[current_node] -= 1
                        deg[neighbor[1][0]] -= 1
                        current_node = neighbor[1][0]
                        list.remove(neighbor)
                        break
        ans.reverse()
        return ans

    def skip(self, circuit):
        weight = 0
        order = []
        cir = circuit
        visited = [0 for _ in range(self.n)]
        c = cir.pop(0)
        first = c
        while len(cir)>=0:
            visited[c] = True
            if cir == []:
                order.append(c)
                order.append(first)
                weight += self.dist[c][first]
                break
            elif visited[cir[0]] == True:
                cir.pop(0)
            else:
                order.append(c)
                cc = cir.pop(0)
                weight += self.dist[c][cc]
                c = cc
        return weight, order

    def directed_degree(self, mst):
        deg = [[0 for _ in range(self.n)],[0 for _ in range(self.n)]] #[[out degree],[in degree]]
        for i in range(len(mst)):
            deg[0][mst[i][1][0]] += 1
            deg[1][mst[i][1][1]] += 1

        return deg

    def directed_sub_graph(self, deg):
        sub = []
        for i in range(self.n):
            for j in range(self.n):
                if deg[0][i] >= deg[1][i] or deg[0][j] <= deg[1][j] or i == j:
                    continue
                sub.append( (self.dist[i][j], (i, j)) )

        sub.sort()
        return sub

    def directed_match(self, sub, deg): #greedy
        matching = []
        for e in sub:
            if deg[0][e[1][0]] < deg[1][e[1][0]] and deg[0][e[1][1]] > deg[1][e[1][1]]:
                matching.append(e)
                deg[0][e[1][0]] += 1
                deg[1][e[1][1]] += 1

        return matching

    def directed_circuit(self, euler_graph, deg):
        ans = []
        stack = []
        list = euler_graph
        current_node = list[0][1][0]
        while deg[0][current_node]>0 or stack != []:
            if deg[0][current_node] == 0:
                ans.append(current_node)
                current_node = stack.pop()
            else:
                stack.append(current_node)
                for neighbor in list:
                    if neighbor[1][0] == current_node:
                        deg[0][current_node] -= 1
                        deg[1][neighbor[1][1]] -= 1
                        current_node = neighbor[1][1]
                        list.remove(neighbor)
                        break
        ans.reverse()
        return ans