def check16(lst):   #list 16.
    count=0
    for l in lst:
        for x in l:
            if x =='x':
                count+=1
    if count==16:
                return True
    else:
        return False

def check(lst):   #how to choose in the list.
    count=0
    lst2=[]
    for l in lst:
        for a in l:
            if(a!='x'):
                lst2.append(a)
    for l in range(0,len(lst2)):
        for m in range(l+1,len(lst2)):   #two adjacent squares are selected.
            if abs(lst2[l]-lst2[m]) == 4 or abs(lst2[l]-lst2[m]) == 1:
                if not((lst2[l]==4 and lst2[m]==5)or(lst2[m]==4 and lst2[l]==5)or(lst2[l]==8 and lst2[m]==9)or(lst2[m]==8 and lst2[l]==9)or(lst2[l]==12 and lst2[m]==13)or(lst2[l]==12 and lst2[m]==13)or lst2[l]>16 or lst2[l]<1 or lst2[m]>16 or lst2[m]<1):
                    return False
    return True
changer = 1
lst=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]   #game board.
print(lst[0])   #first line.
print(lst[1])   #second line.
print(lst[2])   #third line.
print(lst[3])   #fourth line.
while(True):
    if(changer == 1):
        print( 'please player 1 will play : ')   #start playing.. 
        x=int (input())                          #by entering..
        y=int (input())                          #two numbers.
        if(x>16 or x<0 or y>16 or y<0):   #if it goes out of range.
            print('the number is bigger ')
            continue
        if(x==5 and y==4 or x==4 and y==5 or x==8 and y==9 or x==9 and y==8 or x==12 and y==13 or x==13 and y==12 or lst[(x-1)//4][(x%4)-1]=='x' or lst[(y-1)//4][(y%4)-1]=='x'):
            print('wrong positionand not be x')   #if the fields are already selected.
            continue
        
        if abs(x-y)==4 or abs(x-y)==1:   ##if all fields are filled out.
                  lst[(x-1)//4] [x%4-1]='x'
                  lst[(y-1)//4] [y%4-1]='x'
                  print(lst[0])
                  print(lst[1])
                  print(lst[2])
                  print(lst[3])
        if(check16(lst)):
            print ("draw")
            break
        if(check(lst)):
            print('player 1 is the winner ')
            break
            if(abs(temp1-temp2)!=1 or abs(temp1-temp2)!=4):   #if fields are more than 2.
                 print('player 1 is winner')
                 break
            else:
                 continue  
        changer = 2
    elif(changer == 2):   #playing with the second player.
        print('player 2 will play : ' )
        x1=int (input())   #enter two..
        y1=int (input())   #numbers.
        if(x>16 or x<0 or y>16 or y<0):   #if out of range.
            print('wrong inputs')
            continue
        if((x1==5 and y1==4) or (x1==4 and y1==5 )or (x1==8 and y1==9) or (x1==9 and y1==8) or (x1==12 and y1==13) or (x1==13 and y1==12) or lst[(x1-1)//4][(x1%4)-1]=='x' or lst[(y1-1)//4][(y1%4)-1]=='x'):
            print('wrong position and not be x')   #check if the fields are selected.
            continue        
        if abs(x1-y1)==4 or abs(x1-y1)==1:   ##if all fields are filled out.
            lst[(x1-1)//4] [x1%4-1]='x'
            lst[(y1-1)//4] [y1%4-1]='x'
            print(lst[0])
            print(lst[1])
            print(lst[2])
            print(lst[3])
        else:   #if a number is taken out of range.
            print('wrong number and wrong position')
        if(check16(lst)):   
            print ("draw")
            break
        changer = 1
        #break
        if(check(lst)):
            print('player 2 is the winner ')
            break
        
            if(abs(temp1-temp2)!=1 or abs(temp1-temp2)!=4):   ##if 2 fields are more than 1.
                 print('player 2 is winner')
                 break
            else:
                 u=temp1
                 continue

