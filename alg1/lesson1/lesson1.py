def datafile(file):
    f = open(file,'rt',encoding='UTF8')
    while True:
        line = f.readline()
        if not line:
            break
        if line == '\n':
            continue
        lines.append(line.split('\n')[0])
    return lines

def binarysearch(data,target,begin,end):
    if begin > end:
        if data[end]:  #바로 앞 단어가 존재하면
            return end
        else:
            return -1
    else:
        middle = int((begin+end)/2)
        if data[middle] == target:
            return middle
        elif data[middle] > target:
            return binarysearch(data,target,begin,middle-1)
        else:
            return binarysearch(data, target,middle+1, end)


if __name__=="__main__":

    lines = []  # 전체 리스트
    words = []  # 전체 소문자 변환된 단어 리스트
    pos = []  # 품사 리스트

    while True:
        commend = input("$ ")

        if len(commend.split()) == 2:
            second = commend.split()[1]

        first = commend.split()[0]

        if first == "size":
            print(len(lines))

        if first == "read":
            lines = datafile(second)

            for i in lines:
                words.append(i.split()[0].lower())
                pos.append(i.split()[1])

        if first == "find":
            # 인덱스 받아오고, 해당 조건에 맞는 단어 출력
            word = second.lower()
            index = binarysearch(words,word,0,len(words)-1)

            if word in words: # return 값이 middle 일 경우
                print(lines[index])
                cnt = 1

                while True:
                    index = index + 1
                    if word in words[index:]:
                        cnt = cnt + 1
                        print(lines[index])
                    else:
                        break

                print("[Found",cnt,"items.]")

            else:  #return 값이 end 일 경우
                print("[Not found]")
                print(lines[index].split()[0],lines[index].split()[1])
                print("- - -")
                print(lines[index+1].split()[0], lines[index+1].split()[1])

            #print(lines[word_index])
            #print(words[word_index])

        if first == "exit":
            break