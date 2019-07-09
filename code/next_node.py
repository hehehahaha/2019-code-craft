def next_node(input_graph):
    n = len(input_graph)
    save_point = [[-1 for i in range(n)] for j in range(n)]   #创建一个形状等于邻接矩阵大小，值全为-1的列表，用于保存结点值。
    #floyd算法
    for k in range(n):
        for i in range(n):      
            for j in range(n):
                if input_graph[i][j]>input_graph[i][k]+input_graph[k][j]:
                    input_graph[i][j]=input_graph[i][k]+input_graph[k][j]
                    save_point[i][j]=k 
    return save_point

def getRoutes(path,start,end): #最短路径矩阵
    rts = [] #存放路线
    rts1 = []
    rts.append(start)
    i = start
    j = end
    while path[i][j] != -1:
        rts1.append(path[i][j])
        j = path[i][j]
    rts1.reverse()
    rts.extend(rts1)
    rts.append(end)
    return rts

def getPath(rts,path,i,j):
    if path[i][j] == -1:
        rts.append(j)
    else:
        getPath(rts,path,i, path[i][j])
        getPath(rts,path, path[i][j], j)
    #rts.append(j)
    #print(rts)
    return rts
#输入示例
#inf=9999    
#input_graph = [[0, 2, 6, 4], [inf, 0, 3, inf], [7, inf, 0, 1], [5, inf, 12, 0]]
#out = next_node(input_graph)
#rts = []
#out = getPath(rts, out, 1, 3)
#print(out)