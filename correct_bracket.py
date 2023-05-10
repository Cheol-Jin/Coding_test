def solution(s):
    answer = True
    
    point = 0 #괄호 판별용 
    
    s = list(s)
    len_s = len(s)
    
    list1 = []
    
    for i in range(len_s):
        list1.append(s[i])
        if list1[-1] == '(':
            point = point + 1
        elif list1[-1] == ')' and point >= 1:
            list1.pop()
            list1.pop()
            point = point - 1
    
    answer = len(list1) == 0
            
    return answer
