import logging
import sys
import set_graph
import next_node
import get
import numpy as np
import copy
import random
logging.basicConfig(level=logging.DEBUG,
                    filename='.\CodeCraft-2019',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')


def main():
    if len(sys.argv) != 5:
        #logging.info('please input args: car_path, road_path, cross_path, answerPath')
        #exit(1)
        car_path = 'config2/car.txt'
        road_path = 'config2/road.txt'
        cross_path = 'config2/cross.txt'
        preset_answer_path = 'config2/presetAnswer.txt'
        #answer_path = '../config_6/answer.txt'
        answer_path ='D:/华为软挑/code/判题器/CodeCraft2019Judge-Repecharge/config2/answer.txt'
    #car_path = sys.argv[1]
    #road_path = sys.argv[2]
    #cross_path = sys.argv[3]
    #answer_path = sys.argv[4]

    logging.info("car_path is %s" % (car_path)) 
    logging.info("road_path is %s" % (road_path))
    logging.info("cross_path is %s" % (cross_path))
    logging.info("preset_answer_path is %s" % (preset_answer_path))
    logging.info("answer_path is %s" % (answer_path))

    #读出数据并存储为对应的数据结构
    #道路
    road_id, road_len, road_spe, road_num, node_id1, node_id2, road_flag = get.getroad(road_path)
    road_len1 = [0 for i in range(len(road_len))]
    road_len2 = [0 for i in range(len(road_len))]
    road_spe_sum = 0
    for i in range(len(road_len)):
        road_len2[i] = np.sqrt(np.sqrt(road_len[i]))/road_num[i]
        road_len1[i] = np.sqrt(np.sqrt(road_len[i]/road_spe[i]))/road_num[i]
        road_spe_sum += road_spe[i]
    road_spe_pre = road_spe_sum/len(road_len)  #道路平均限速
    print(road_spe_pre)
    #路口
    crossList = get.getcross(cross_path)
    #车信息
    carID, car_ori, car_ter, car_spe, car_tim, car_pri = get.getcar(car_path)
    #预置车辆
    pre_car_id, pre_car_time = get.getpreset(preset_answer_path)
    #重新获取结点ID
    node_id1, node_id2, car_ori, car_ter = get.refineID(crossList, node_id1, node_id2, car_ori, car_ter)
    #设置道路编号表
    set_road_matrix = set_graph.road_matrix(road_id, node_id1, node_id2)
    #创建邻接表
    graph1 = set_graph.set_graph(node_id1, node_id2, road_len1, road_flag, len(crossList))
    graph2 = set_graph.set_graph(node_id1, node_id2, road_len2, road_flag, len(crossList))
    #创建结点表
    save_point1 = next_node.next_node(graph1)
    save_point2 = next_node.next_node(graph2)
    print('pre time max: ' , max(pre_car_time))
    out_list = [[] for j in range(len(carID))]
    out_list1 = [[] for j in range(len(carID))]  #[[10000, 5024, 5025, 5031, 5042, 5053],
    for k in range(len(carID)):
        lis1 = [car_ori[k]]
        path1 = next_node.getPath(lis1,save_point1,car_ori[k],car_ter[k])
        #print(path)
        #输出每辆车路径
        out_path1 = [0 for i in range(len(path1)-1)]
        for i in range(len(path1)-1):
            out_path1[i]=set_road_matrix[path1[i]][path1[1+i]]
    #for i in
        out_path1.insert(0,carID[k])
        #print(out_path)
        out_list1[k] = out_path1

    out_list2 = [[] for j in range(len(carID))]
    for k in range(len(carID)):
        lis2 = [car_ori[k]]
        path2 = next_node.getPath(lis2,save_point2,car_ori[k],car_ter[k])
        #print(path)
        #输出每辆车路径
        out_path2 = [0 for i in range(len(path2)-1)]
        for i in range(len(path2)-1):
            out_path2[i]=set_road_matrix[path2[i]][path2[1+i]]
    #for i in
        out_path2.insert(0,carID[k])
        #print(out_path)
        out_list2[k] = out_path2
    #print(time_of_pre)
    for i in range(len(carID)):
        if car_spe[i] >= road_spe_pre:
            out_list[i] = out_list1[i]
        else:
            out_list[i] = out_list1[i]
    car_spe_arry = np.array(car_spe)
    carID_arry = np.array(carID)
    car_pri_arry = np.array(car_pri)
    pre_car_time_sum = 0
    for i in range(len(pre_car_time)):
        pre_car_time_sum += pre_car_time[i]
    pre_sum = pre_car_time_sum/len(pre_car_time)
       
    #distance = [] #最短路径距离
    #for i in range(len(car_ori)):
    #    distance.append(graph[car_ori[i]][car_ter[i]])
    #sum_time = []  #总时间
    #for i in range(len(car_ori)):
    #    sum_time.append(graph[car_ori[i]][car_ter[i]]/car_spe[i])   
    #arrive_time = []   #到达时间
    #for i in range(len(car_ori)):
    #    arrive_time.append(sum_time[i]+car_tim[i])   
    #out_list[0].insert(1,car_ori[0])
    #for i in range(1,len(out_list)):
    #    out_list[i].insert(1,int(max(car_ori[i],i)))
    #tim_and_num = get.precar(pre_car_time)
    #print(tim_and_num)
    #del_pre = get.delpre(out_list, pre_car_id)
    #car_tim_change = get.delprecartime(carID, car_tim, pre_car_id)

    #xishu = int(len(out_list)/40)
    #random1 = []
    ##random = np.random.randint(max(pre_car_time)+5, max(pre_car_time)+5+xishu, len(out_list))
    #for i in range(len(out_list)):
    #    bbbb = random.randrange(max(pre_car_time)+5, max(pre_car_time)+5+xishu, 5)
    #    random1.append(bbbb)
    #print(max(car_tim))
    for i in range(len(out_list)):
        out_list[i].insert(1,max(car_tim[i], 20+max(pre_car_time)+speed_sort_id[carID[i]]))         
    get.answer(answer_path, out_list)

if __name__ == "__main__":
    main()