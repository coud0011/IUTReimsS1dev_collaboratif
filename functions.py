def convert(n : int,b : int) -> str:

    reste=''
    val=0
    while n >= b:
        val = ( n % b)
        reste+= str(val)
        n= n//b

    reste+= str(n)
    print (reste[::-1])


convert(7,3)