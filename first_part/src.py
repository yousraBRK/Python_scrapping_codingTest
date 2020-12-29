import sys

def exercise_one():

    for i in range(100) :
        if (i%3 == 0 and i%5 == 0) :
            print ("ThreeFive")
        elif(i%3 ==0) :
                print ("Three")
        elif(i%5==0) :
                print("Five")
        else :
                 print(i)

        
    pass

def exercise_two(num):

    Numberlist = [int(x) for x in str(num)] 

    
   #Step 1 : check if the number contains duplicate digits

    for  i in range(len(Numberlist)):    
        number=Numberlist[i]

        for j in range(i+1,len(Numberlist)) :
             if(number == Numberlist[j]) :

                    sys.exit("NOT COLORFUL " + str(number)+" is duplicate")
                    return 0
                    
    #Step 2 : check the multiplication of each subset

    for i in range(len(Numberlist)-1) :                
        number = Numberlist[i]*Numberlist[i+1]   
        print(number)  
       

        for  j in range(i+2,len(Numberlist)):

            if (number not in Numberlist):
                Numberlist.append(number)
                number=number*Numberlist[j]
            else :
                
                sys.exit("NOT COLORFUL " + str(number)  +" is duplicate") 
                return 0                                  
         
    print("THE NUMBER IS COLORFUL")
pass

def calculate(element):

    if not isinstance(element,list) :
        print("False")
        return False
    else :
        sum=0
        for i in range(len(element)) :
            if isinstance(element[i],str):
                if(element[i].isnumeric()) :
                    sum = sum + int(element[i])
    print(sum)
    return sum 

def anagrams(word,vec):
    anagramsVec =[]
    for i in range(len(vec)):
        if (len(word) == len(vec[i])) and  (sorted(word) == sorted(vec[i]))  :
            anagramsVec.append(vec[i])
    
    print(anagramsVec)


#exercise_one()
#exercise_two(2532)
#calculate(['biche','2',2,'3','1'])
#anagrams('laser', ['lazing', 'lazy',  'lacer'])

