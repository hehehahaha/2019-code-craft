import numpy as np
def getroad(road_path):
    with open(road_path,'r') as roadDataFile:
        roadData = roadDataFile.read().splitlines()
    length = len(roadData)
    road_id = []  
    road_len = []   
    road_spe = []   
    road_num = []   
    node_id1 = []   
    node_id2 = []   
    road_flag = []  
    for i in range(length):
        if roadData[i][0] == '#':
            continue
        roadInfo = tuple(eval(roadData[i]))
        road_id.append(roadInfo[0])
        road_len.append(roadInfo[1])
        road_spe.append(roadInfo[2])
        road_num.append(roadInfo[3])
        node_id1.append(roadInfo[4])
        node_id2.append(roadInfo[5])
        road_flag.append(roadInfo[6])
    return road_id,road_len,road_spe,road_num,node_id1,node_id2,road_flag

def getcross(cross_path):
    with open(cross_path,'r') as crossDataFile:
        crossData = crossDataFile.read().splitlines()
    length = len(crossData)
    crossList = []
    for i in range(length):
        if crossData[i][0] == '#':
            continue
        crossInfo = tuple(eval(crossData[i]))
        crossList.append(crossInfo[0])
    return crossList

def getcar(car_path):
    with open(car_path,'r') as carDataFile:
        carData = carDataFile.read().splitlines()
    length = len(carData)
    carID = []  
    car_ori = []   
    car_ter = []   
    car_spe = []   
    car_tim = []  
    car_pri = [] 
    for i in range(length):
        if carData[i][0] == '#':
            continue    
        carInfo = tuple(eval(carData[i]))
        if carInfo[6] == 0:
            carID.append(carInfo[0])
            car_ori.append(carInfo[1])
            car_ter.append(carInfo[2])
            car_spe.append(carInfo[3])
            car_tim.append(carInfo[4])
            car_pri.append(carInfo[5])
    return carID,car_ori,car_ter,car_spe,car_tim,car_pri

def getpreset(pre_path):
    with open(pre_path,'r') as preDataFile:
        preData = preDataFile.read().splitlines()
    length = len(preData)
    pre_carid = []  
    pre_car_time = []   
    #car_ter = []   
    #car_spe = []   
    #car_tim = []   
    for i in range(length):
        if preData[i][0] == '#':
            continue    
        preInfo = tuple(eval(preData[i]))
        pre_carid.append(preInfo[0])
        pre_car_time.append(preInfo[1])
        #car_ter.append(carInfo[2])
        #car_spe.append(carInfo[3])
        #car_tim.append(carInfo[4])
    return pre_carid, pre_car_time

def answer(answer_path,a):
    with open(answer_path,'w') as answerFile:
        for i in range(len(a)):
            answerFile.write('(')
            for j in range(len(a[i])):
                answerFile.write('%d' % a[i][j])
                if j != len(a[i])-1:
                    answerFile.write(',')
            answerFile.write(')\n')

def refineID(crossList,node_id1,node_id2,car_ori,car_ter):
    for i in range(len(node_id1)):
        node_id1[i] = crossList.index(node_id1[i])
        node_id2[i] = crossList.index(node_id2[i])   
    for i in range(len(car_ori)):
        #node_id1[i] = crossList.index[i]
        car_ori[i] = crossList.index(car_ori[i])
        car_ter[i] = crossList.index(car_ter[i])
    return node_id1,node_id2,car_ori,car_ter

def duplicate_removal(lt):
    lt1 = []
    for i in lt:
        if i not in lt1:
            lt1.append(i)
    return lt1

def precar(pre_car_time):  #{1: 80, 6: 80, 
    pre_time_copy = np.array(pre_car_time)
    pre_time_copy = np.unique(pre_time_copy)
    number_of_precar = [0 for i in range(pre_time_copy.size)]
    for k in range(pre_time_copy.size):
        number_of_precar[k] = np.sum(pre_car_time == pre_time_copy[k])
    return dict(zip(pre_time_copy,number_of_precar))

def car_time_test(car_id, car_spe, car_pri, pre_tim):
    car_spe_copy = np.unique(car_spe)
    car_spe_copy6 = sorted(car_spe_copy, reverse=True)

    speed_sort_id = {}
    time = 1
    car_out = 0
    for j in range(len(car_spe_copy6)):
        for i in range(len(car_spe)):
            if car_pri[i] == 1:
                if car_spe[i] == car_spe_copy6[j]:
                    car_out = car_out + 1
                    speed_sort_id.update({car_id[i]:time})
                    if car_out>30 and time < 60:
                        car_out = 0
                        time = time + 1
                    if car_out>20 and time >= 60 and time < 200:
                        car_out = 0
                        time = time + 1  
                    if car_out>19 and time >= 200 and time < 300:
                        car_out = 0
                        time = time + 1                                
                    if car_out>18 and time >= 300:
                        car_out = 0
                        time = time + 1   
    time = time + 70
    time1 = time
    print('youxian time: ' , time+pre_tim)
    for j in range(len(car_spe_copy6)):
        for i in range(len(car_spe)):
            if car_pri[i] == 0:
                if car_spe[i] == car_spe_copy6[j]:
                    car_out = car_out + 1
                    speed_sort_id.update({car_id[i]:time})
                    if car_out>30 and time < time1+60:
                        car_out = 0
                        time = time + 1
                    if car_out>25 and time >= 60+time1 and time < 200+time1:
                        car_out = 0
                        time = time + 1        
                    if car_out>20 and time >= 200+time1 and time < 400+time1:
                        car_out = 0
                        time = time + 1  
                    if car_out>20 and time >= 400+time1 and time < 950+time1:
                        car_out = 0
                        time = time + 1  
                    if car_out>18 and time >= 950+time1:
                        car_out = 0
                        time = time + 1   
    print('wancheng time: ', time+pre_tim)                     
    return speed_sort_id

def car_time_test1(car_id, car_spe, car_pri, pre_tim):
    car_spe_copy = np.unique(car_spe)
    car_spe_copy6 = sorted(car_spe_copy, reverse=True)

    speed_sort_id = {}
    time = 1
    car_out = 0
    for j in range(len(car_spe_copy6)):
        for i in range(len(car_spe)):
            if car_pri[i] == 1:
                if car_spe[i] == car_spe_copy6[j]:
                    car_out = car_out + 1
                    speed_sort_id.update({car_id[i]:time})
                    if car_out > 38 and time < 30:
                        car_out = 0
                        time = time + 1
                    if car_out > 15 and time >= 30 and time < 50:
                        car_out = 0
                        time = time + 1
                    if car_out > 31 and time >= 50 and time < 100:
                        car_out = 0
                        time = time + 1
                    if car_out > 28 and time >= 100:
                        car_out = 0
                        time = time + 1                        
    time = time + 25
    time1 = time
    print('youxian time: ' , time+pre_tim)
    for j in range(len(car_spe_copy6)):
        for i in range(len(car_spe)):
            if car_pri[i] == 0:
                if car_spe[i] == car_spe_copy6[j]:
                    car_out = car_out + 1
                    speed_sort_id.update({car_id[i]:time})
                    if car_out>30 and time < time1+50:
                        car_out = 0
                        time = time + 1
                    if car_out>30 and time >= 50+time1 and time < 100+time1:
                        car_out = 0
                        time = time + 1       
                    if car_out>25 and time >= 100+time1 and time < 400+time1:
                        car_out = 0
                        time = time + 1                                 
                    if car_out>25 and time >= 400+time1 and time < 800+time1:
                        car_out = 0
                        time = time + 1   
                    if car_out>22 and time >= 800+time1:
                        car_out = 0
                        time = time + 1                                    
    print('wancheng time: ', time+pre_tim)         
    return speed_sort_id