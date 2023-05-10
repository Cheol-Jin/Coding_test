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

    return time

            
#시간복잡도 N^2


def solution(bridge_length, weight, truck_weights):
    bridge = [0 for _ in range(bridge_length)]
    bridge = deque(bridge)

    i = 0
    time = 0
    already = [] #이미 들어온 트럭
    count = 0 #트럭 모두 들어온 후의 연산을 위해 설정
    bridge_sum = 0

    while True:
        bridge_sum -= bridge[-1]
        bridge.pop()

        if bridge_sum + truck_weights[i] <= weight and len(already) != len(truck_weights): #다음 트럭이 들어와도 무게가 안 넘치고, 아직 모든 트럭이 들어오지 않았을 때
            bridge.insert(0, truck_weights[i])
            already.append(truck_weights[i])
            bridge_sum += truck_weights[i]

        elif len(already) == len(truck_weights): #마지막 트럭이 들어온 후
            bridge.appendleft(0) 

        elif bridge_sum + truck_weights[i] > weight: #다음 트럭이 들어오면 무게가 넘치는 경우 
            bridge.appendleft(0)
            if bridge_sum + truck_weights[i] <= weight: #트럭이 한 칸씩 이동했을 시 무게가 넘치지 않는 경우
                bridge.popleft()
                bridge.appendleft(truck_weights[i])
                already.append(truck_weights[i]) 
                bridge_sum += truck_weights[i]       
            else:
                i = i - 1
    
        if len(already) == len(truck_weights): #마지막 트럭이 들어온 후
            count = count + 1
        if count == bridge_length: #마지막 트럭이 다리를 지나갔을 때 while문 탈출
            time = time + 2
            break 
        
        time = time + 1
        if i < len(truck_weights) - 1:
            i = i + 1
    return time

#시간 복잡도 N 으로 다시 풀어 정답
            
    
