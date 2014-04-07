#finds the term to the multiples of 5, 
i=1
j=0
x=0
while x<4000:
     x=5*i
     i=i+1
     if x==4000:
               break     
     j=j+x
     
print "the sum of multiples of 5, if the last multiple of 5 <4000 is", j
   
    

