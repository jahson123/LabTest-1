num = int(input("Input number: "))

def count(num):
    binary = ""
    bit = 0
    if(num != 0):
        while( num >=1):
            if (num %2 == 0 ):
                binary = binary + "0"
                num /= 2
            else:
                binary = binary + "1"
                bit += 1
                num = (num-1) /2
    else:
        bit = 0
    print("Binary Number : " + binary)
    print(f'Number of bits {bit}')
    
count(num)
    
