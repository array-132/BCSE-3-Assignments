def xor(a,b):
    """
    To calculate xor of two bit streams, given as strings.
    We add zeroes to the left of the smaller string, so that xor of all bit points can be calculated.
    """
    m=''
    x = len(a)
    y = len(b)
    if x < y:
        a = '0'*(y-x) + a
    else: 
        b = '0'*(x-y) + b

    for i in range (0,len(a)):
        if(a[i] == b[i]):
            m += '0'
        else : 
            m += '1'
    return m



def crc(generator_polynomial,original_message):
    n = len(generator_polynomial)
    extended_message = original_message + '0'*(n-1)
    number_of_operations = len(extended_message) - n + 1
    for _ in range (n,len(extended_message)):
        

                
