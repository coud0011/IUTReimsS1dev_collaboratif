def convert(n : int,b : int) -> str:

    reste=''
    val=0



    while n+b-1 >= b:
        
        val = ( n % b)

        if val == 10:
            reste+="A"
        elif val == 11:
            reste+="B"
        elif val == 12:
            reste+="C"
        elif val == 13:
            reste+="D"
        elif val == 14:
            reste+="E"
        elif val == 15:
            reste+= "F"
        else:
            reste+= str(val)

        n= n//b


    print (reste[::-1])


convert(7,3)