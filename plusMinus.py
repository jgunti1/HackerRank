def plusMinus(array):
    neg = 0
    pos = 0
    zero = 0
    length = len(array)
    for i in array:
        if i<0:
            neg += 1
        elif i>0:
            pos += 1
        else:
            zero += 1
    
    print(round(pos/length,6))
    print(round(neg/length,6))
    print(round(zero/length,6))
    
    
def main():
    plusMinus([-4,3,-9,0,4,1])
    
    
            
            
            