def solution(participant, completion):
    answer = ''
    

    dict_p = Counter(participant)
    dict_c = Counter(completion)
     
    for key in dict_p:
        if dict_p[key] != dict_c[key]:
            answer = key

    return answer
  
  #Collection 모듈의 ounter 클래스: 중복된 데이터가 포함된 배열을 넘기면, 각 원소가 몇번 나왔는지 카운트 해줌
