memory = list(map(str, input().split())) 

def solution(memory):

    memory_len = len(memory)

    result = ''
    re_index = 0

    for i in range(memory_len):
        if memory[i] == 'BOOL': #1바이트
            if re_index % 8 == 0: #8바이트마다 , 추가
                result = result + ','
            result = result + '#'
            re_index += 1

        elif memory[i] == 'SHORT': #2바이트
            if re_index % 2 != 0:
                result = result + '.'
                re_index += 1
            if re_index % 8 == 0: #8바이트마다 , 추가
                result = result + ','
            result = result + '##'
            re_index += 2

        elif memory[i] == 'FLOAT': #4바이트
            if re_index % 4 != 0:
                while(re_index % 4 != 0):
                    result = result + '.'
                    re_index += 1
            if re_index % 8 == 0 and i != 0: #8바이트마다 , 추가
                result = result + ','
            result = result + '####'
            re_index += 4
                
        elif memory[i] == 'INT': #8바이트
            if re_index % 8 != 0:
                while(re_index % 8 != 0):
                    result = result + '.'
                    re_index += 1
            if i != 0: #8바이트마다 , 추가
                result = result + ','
            result = result + '########'
            re_index += 8

        elif memory[i] == 'LONG': #16바이트
            if re_index % 8 != 0:
                while(re_index % 8 != 0):
                    result = result + '.'
                    re_index += 1
            if i != 0: #8바이트마다 , 추가
                result = result + ','
            result = result + '########,########'
            re_index += 16
        
        
        if re_index % 8 != 0 and i == memory_len - 1:
            while re_index % 8 != 0:
                result = result + '.'
                re_index += 1

    if re_index > 128:
        mess = 'HALT'
        return mess
    
    return result

print(solution(memory))
