# Copyright 2021 AXEL COUDROT et TOM DARET
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
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

def printRectangle(width: int, height: int) :
    i=0
    j=0
    while i < height:
        form=''
        j=0
        while j < width:
            form+="*"
            j+=1
        print(form)
        i+=1




def printTriangle(size: int) :
    Tri="*"
    while size>=1 :
        print(Tri)
        Tri+="*"
        size=size-1
>>>>>>> f3aa3cb193813d8bfff744c8a8d3b9b60143f2d2
