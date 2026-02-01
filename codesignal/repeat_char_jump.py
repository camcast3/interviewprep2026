def repeat_char_jump(inputString, k):
    # TODO: Implement the solution to generate n-length string as per given instructions.
    result = ''
    length = len(inputString)
    visited = [False] * length
    i = 0
    
    while not visited[i]:
        
        result += inputString[i]
        visited[i] = True
        
        i = (i + k) % length
    
    return result
    
