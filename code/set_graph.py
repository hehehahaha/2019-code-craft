def road_matrix(road_id,node_id1,node_id2):
    set_road_matrix = [[-2 for i in range(len(node_id1))] for j in range(len(node_id1))]#道路编号与结点表
    for i in range(len(node_id2)):
        set_road_matrix[node_id1[i]][node_id2[i]] = set_road_matrix[node_id2[i]][node_id1[i]] = road_id[i]
    return set_road_matrix

def set_graph(u, v, w, flag, num):
    inf = 9999
    #初始化
    graph = []
    for i in range(num):
        graph += [[]]
        for j in range(num):
            if i == j:
                graph[i].append(0)
            else:
                graph[i].append(inf)
    
    #建立邻接表
    for i in range(len(u)):
        #u, v, w = input().strip().split()
        if flag[i] == 0:
            graph[u[i]][v[i]] = w[i]
        elif flag[i] == 1:
            graph[u[i]][v[i]] = w[i]
            graph[v[i]][u[i]] = w[i]
        else:
            break
    return graph

#输入示例
#flag = [1,0,1,1,0,0,0,0,1]    #0为从u结点到v结点单向，1为双向
#u = [0,0,1,1,2,2,2,5,6]     #结点1，需要给结点重新编号, ID从0开始递增 
#v = [1,2,2,3,4,5,6,6,7]     #结点2，ID从0开始
#w = [5,1,2,5,1,3,2,6,1]     #权值
#num = 8         #一共有几个结点，与u、v长度不同
#graph = set_graph(u, v, w, flag, num)
#print(graph)

