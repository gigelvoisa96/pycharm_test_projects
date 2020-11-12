def adddirected2charsfromlimit(char_list, index_of_chars, direction=0):
    returned_string=""
    if direction == 0:
        range_list = range(0, index_of_chars)
    elif direction == 1:
        range_list = range(len(char_list)-index_of_chars, len(char_list))
    for i in range_list:
        returned_string+=char_list[i]
    return returned_string


def my_functionl05_01(my_string):
    char_list=list(my_string)
    if len(char_list)<2:
        print("Șirul este prea scurt.")
        return
    new_string="" + adddirected2charsfromlimit(char_list, 2, 0) + adddirected2charsfromlimit(char_list, 2, 1)
    print(new_string)



def do_problem01():
    my_functionl05_01("s")


def my_function_l05_01(my_string):
    char_list = list(my_string)
    kounter=0
    for char in char_list: kounter+=1
    print(kounter)


def do_problem02():
    my_function_l05_01("student")


def getlungime(my_string):
    kounter=0
    for i in list(my_string): kounter+=1
    return kounter


def createCharList(my_string):
    return list(my_string)


def my_function_l05_03(my_string):
    lung = getlungime(my_string)
    char_list = createCharList(my_string)
    new_string=""
    for i in range(0, lung):
        if i%2==0:  new_string+=char_list[i]
    print(new_string)


def do_problem03():
    my_function_l05_03('String!')


def getCharsParity(char_list, length, equality_condition):
    parity_chars_list=[]
    for i in range(0,length):
        if i%2==equality_condition: parity_chars_list.append(char_list[i])
    return parity_chars_list


def my_function_l05_04(my_string):
    lungime = getlungime(my_string)
    # print(getCharsParity(createCharList(my_string), lungime, 0))
    new_string ="".join(getCharsParity(createCharList(my_string), lungime, 1))
    print(new_string)


def do_problem04():
    my_function_l05_04('String!')


def my_function_l05_05(my_string):
    lungime = getlungime(my_string)
    char_list = createCharList(my_string)
    kount_upper=0
    total_kount=lungime
    for i in range(0,lungime):
        if (""+char_list[i]).isupper(): kount_upper+=1
    new_string=""
    if total_kount/4 <= kount_upper:
        for i in range(0,lungime):
            if(""+char_list[i]).isupper():
                char_list[i]=(''+char_list[i]).lower()
                new_string += char_list[i]
                continue
            if(""+char_list[i]).islower():
                char_list[i]=(''+char_list[i]).upper()
                new_string += char_list[i]
    print(new_string)


def do_problem05():
    my_function_l05_05('MySQL')


def isALittleString(my_string):
    if getlungime(my_string)<4:
        return True
    else:
        return False


def has_startWithPrefix(my_string, prefix):
    char_list = createCharList(my_string)
    kount=0
    for i in range(0, getlungime(prefix)):
        if(char_list[i] == prefix[i]): kount+=1
    print("kount", kount)
    if kount==getlungime(prefix): return True
    else: return False



def my_function_l05_06(my_string, prefix, sufix):
    if isALittleString(my_string):
        print('Sir prea scurt')
    else:
        if has_startWithPrefix(my_string, prefix):
            new_string="" + my_string + sufix
        else:
            new_string="" + prefix + my_string
        print(new_string)


def do_problem06():
    my_function_l05_06('examinare', 're', 'e')


def isPar(valoare):
    if valoare%2==0: return True
    else: return False


def my_function_l05_07(my_str, insertString):
    lungime = getlungime(my_str)
    char_list = createCharList(my_str)
    if lungime<2: print('text prea scurt')
    elif isPar(lungime): char_list[(lungime-1)//2]=""+char_list[(lungime-1)//2]+insertString
    else: char_list[(lungime-1)//2+1] = ""+char_list[(lungime-1)//2]+insertString
    new_string=""
    for char in char_list:
        new_string+=char
    print(new_string)



def do_problem07():
    my_function_l05_07('ab', 'cc')


def invers(my_string):
    new_string = ""
    char_list = createCharList(my_string)
    lungime = getlungime(my_string)
    for i in range(lungime-1, -1, -1):
        new_string+=char_list[i]
    return new_string


def my_function_l05_08(my_string):
    lungime=getlungime(my_string)
    if lungime%4==0:
        print(invers(my_string))
    elif lungime%3==0:
        print("".join(getCharsParity(createCharList(my_string), lungime, 0)))
    else:
        print(my_string)


def do_problem08():
    my_function_l05_08('abcd')



if __name__ == '__main__':
    do_problem01()
    do_problem02()
    do_problem03()
    do_problem04()
    do_problem05()
    do_problem06()
    do_problem07()
    do_problem08()