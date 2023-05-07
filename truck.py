from collections import deque

def solution(bridge_length, weight, truck_weights):
    weight_sum = 0
    
    bridge = [0] * bridge_length
    time = 0
    i = 0
    last = 0 
    
    bridge[0] = truck_weights[0] #while문 조건 맞추기위해 인덱스 0인 원소 먼저 넣기
    
    while(sum(bridge) != 0): #트럭 모두 지나갈 때 까지 
        if i != 0 :
            for j in range(bridge_length-1,-1,-1): #한 사이클마다 끝 인덱스부터
                if j != bridge_length - 1: #한칸씩 이동
                    bridge[j+1] = bridge[j]
                    bridge[j] = 0
                elif j == bridge_length - 1:
                    bridge[bridge_length-1] = 0
                    
        if i == len(truck_weights)-1 and sum(bridge) == 0 and last == 1:
            time = time + 1
            break
                
        if i != 0 and sum(bridge) + truck_weights[i] <= weight: #새로운 원소 들어올 시 이동하면 안됨
            bridge[0] = truck_weights[i]
            if i == len(truck_weights) - 1:
                last = last + 1
        elif i != 0 and sum(bridge) + truck_weights[i] > weight:
            i = i - 1 
                    
        time = time + 1
        if i < len(truck_weights)-1:
            i = i + 1
            
#시간복잡도 N^2
            

    return time
