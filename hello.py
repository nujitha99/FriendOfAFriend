gm = [[0,1,1,1,0],
      [1,0,0,1,0],
      [1,0,0,0,1],
      [1,1,0,0,0],
      [0,0,1,0,0]]

temp1 = []
temp2 = []

p1 = int(input('Please enter first persons index : '))
p2 = int(input('Please enter second persons index : '))

def checkPersonOne(): #check if 'p2' is a friend of 'p1'
    if gm[p1][p2] == 1:
        return True

def checkPersonTwo(): #check if 'p1' is a friend of 'p2'
    if gm[p2][p1] == 1:
        return True
    
            
def checkBoth(): #check if above condition is valid
    first = checkPersonOne()
    second = checkPersonTwo()
    if first and second == True:
        print("Direct friends")
    else:
        for i in gm[p2]: #check if person two has friends
            if i == 1:
                index1 = gm[p2].index(i)
                temp1.append(index1)
        for j in gm[p1]: #check if person one has friends
            if j == 1:
                index2 = gm[p1].index(j)
                temp2.append(index2)
        commonList = list(set(temp1) and set(temp2)) #check for the common friends
        if 1 in commonList:
            print('found a friend in common')
        else:
            print('no such friend in common')
            



checkBoth(); 
