def RepeatCharacter(str,c,n):
    if str == '':
       return None
    str = str[:len(str)//2] + c*n + str[len(str)//2:]
    return str
