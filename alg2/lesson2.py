import math

#변수선언
xl = []
yl = []
lucky = []
nxl = []
nyl = []
num = 0
linecnt = 0
min = 0
min_index = 0

def datafile(file):
    global num
    global xl
    global yl
    count = 0
    f = open(file ,'rt' ,encoding='UTF8')
    line = f.readline()
    num = int(line)
    while True:
        line = f.readline()
        if not line:
            break
        if line == '\n':
            continue
        line = line.split('\n')[0]
        count = count + 1
        #print(line)
        xl.append(int(line.split()[0]))
        #print(xl)
        yl.append(int(line.split()[1]))
        #print(yl)
        if(count == num):
            break
        f.close()
    return


def swap(k,i):
    temp = xl[k]
    xl[k] = xl[i]
    xl[i] = temp

    temp = yl[k]
    yl[k] = yl[i]
    yl[i] = temp


def perm(k):
    global num
    global linecnt
    global  lucky
    cal_result = 0
    temp_result = 0

    if(k==num):
        linecnt = linecnt + 1

        for i in range(0,num):
            #print("[",linecnt,"]  (",xl[i],",",yl[i],")","(index: ",i," K: ",k,","," NUM: ",num,")")
            lucky.append(xl[i])
            lucky.append(yl[i])

        lucky.append(linecnt)
        lucky.append("divide"+str(linecnt))

        #rint(lucky)
        cal_result = cal()
        #print("-------------------------------------------------------------------")
        #print("----------result:",cal_result,"------------------------------------")
        min_check(cal_result,linecnt)
        return
    else:
        for i in range(k,num):
            swap(k,i)
            perm(k+1)
            swap(k,i)




def cal():
    temp = 0
    re_temp = 0
    for i in reversed(range(num)):
        if(i==0):
            break
        else:
            a = xl[i]-xl[i-1]
            #print("A:",a)
            b = yl[i]-yl[i-1]
            #print("B:",b)
            temp =  math.sqrt((a * a) + ( b * b))
            #print("c:",temp)
            re_temp = re_temp + temp

    aa = xl[0]-xl[num-1]
    bb = yl[0]-yl[num-1]
    temp2 = math.sqrt((aa*aa) + (bb*bb))
    #print("temp2: ", temp2)
    re_temp = re_temp + temp2

    #print("resu:",re_temp)
    return re_temp


def min_check(n,index):  #최솟값 구해주는 함수
    global min
    global min_index
    if( min == 0 ):
        min =  n
        min_index = index
    else:
        if(min > n):
            min = n
            min_index = index

    return


def indexdef(index):
    global nxl
    global nyl
    min_target = (((num * 2) + 2) * (index-1))
    destination =(((num * 2) + 2) * index)-2
    for i in range(min_target,destination):
        #print("[",lucky[i],"]")
        if i%2 == 0:
            nxl.append(int(lucky[i]))

        else:
            nyl.append(int(lucky[i]))

def ordered_num():

    for i in range(0,num):
        che1 = nxl[i]
        che2 = nyl[i]

        for j in range(0,num):
            if(che1 == xl[j] and che2 == yl[j]):
                print(j)
            else:
                continue


if __name__=="__main__":

    while True:
        commend = input("$ ")

        if len(commend.split()) == 2:
            second = commend.split()[1]

        first = commend.split()[0]

        if first == "read":
            datafile(second)
            k = 0
            perm(k)
            print("answer:")
            print(min)
            print("index:")
            print(min_index)
            indexdef(min_index)
            #test()
            print("ordered_num:")
            ordered_num()


        if first == "exit":
            break





