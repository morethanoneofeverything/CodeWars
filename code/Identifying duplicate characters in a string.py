def is_isogram(string):

    lower = string.lower()

    if string == '':
        return True
        
    count = {}
    for s in lower:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    for key in count:
        if count[key] > 1:
            return False
       
    return True
    

is_isogram('hello')
is_isogram('luke')
            
