def my_function01(my_string):
    chars = list(my_string)
    #print("characters: len", len(chars))
    print(len(chars))


"""Scrieți o funcție care afișează lungimea unui string primit ca parametru.
       For example:

       Test	                    Result
       my_function("lungime șir")  11
"""
def problema1():
    my_function01("lungime sir")
def my_function02(my_string):
    #Scrieți o funcție care afișează numărul de caractere 'i' pe care le conține șirul primit ca parametru.
    chars = list(my_string)
    k=0
    for i in range(0,len(chars)):
        if("i" == chars[i]): k=k+1
    print(k)


"""
        Scrieți o funcție care afișează 
        numărul de caractere 'i' pe care le conține șirul primit ca parametru.
        For example:

        Test	Result
        my_function("Studenți extraordinari!")
        3

    """
def problema2():
    my_function02("lungime sir")
def my_function03(my_string):
    #Scrieți o funcție care afișează numărul de caractere 'i' pe care le conține șirul primit ca parametru.
    my_function02(my_string)


"""Scrieți o funcție care afișează numărul de caractere 'i' pe care le conține șirul primit ca parametru.
        For example:

        Test	Result
        my_function("Studenți extraordinari!")
        3
"""
def problema3():
    #Scrieți o funcție care afișează numărul de caractere 'i' pe care le conține șirul primit ca parametru.
    my_function03("Studenți extraordinari!")
def my_function04(my_string):
    chars = list(my_string)
    for i in range(0, len(chars)):
        if("s"== chars[i]):
            chars[i] = "*"
    res_string = "".join(chars)
    print(res_string)
"""Scrieți o funcție care afișează șirul primit ca parametru de intrare modificat, după următoarea regulă: toate caracterele 's' sunt înlocuite cu caracterul '*'.
For example:

Test	Result
my_function("student")
*tudent
"""
def problema4():
    #Scrieți o funcție care afișează șirul primit ca parametru de intrare modificat, după următoarea regulă: toate caracterele 's' sunt înlocuite cu caracterul '*'
    my_function04("student")

#Scrieți o funcție care afișează șirul primit ca parametru de intrare modificat,
# după următoarea regulă: toate caracterele 's' sunt înlocuite cu caracterul '*' mai puțin prima apariție a caracterului 's'.
def my_function05(my_string, my_char):
    chars=list(my_string)
    new_string = ""
    first=-1
    for i in range(0, len(chars)):
        if ((first != -1) and (chars[i] == "s")):
            chars[i] = '*'
        if(chars[i]=="s"): first=i
        new_string+=chars[i]
    print(new_string)

"""Scrieți o funcție care afișează cele două șiruri primite ca parametrii concatenate cu spațiu între ele, 
iar prima literă a celor două șiruri sunt interschimbate.
For example:

Test	Result
my_function("bb", "aa")
ab ba
"""
def my_function06(first_string, second_string):
    first_str_chars=list(first_string)
    second_str_chars=list(second_string)
    new_string=""
    if len(first_str_chars) > 0 and 0 < len(second_str_chars):
        first_str_chars[0], second_str_chars[0] = second_str_chars[0], first_str_chars[0]
    new_string+="".join(first_str_chars) + " " + "".join(second_str_chars)
    print(new_string)

"""Scrieți o funcție care afișează șirul primit ca parametru de intrare modificat, după următoarea regulă: toate caracterele 's' sunt înlocuite cu caracterul '*' mai puțin prima apariție a caracterului 's'.
For example:
Test	Result
my_function("student senator", "s")
student *enator
"""
def problema5():
    my_function05("student senator", "s");
    #output:student *enator


def problema6():
    my_function06("bb", "aa")

"""Scrieți o funcție care primește ca parametru de intrare un șir și un număr ce reprezintă al câtelea caracter din șir trebuie eliminat. 
Se va modifica șirul astfel încât să nu conțină acel caracter și se va afișa șirul rezultatul.
For example:
Test	Result
my_function('String!', 5)
Strig!
"""
def my_function07(my_string, index_from_my_string):
    chars = list(my_string)
    new_string=""
    for i in range(0, index_from_my_string-1):
        new_string+=chars[i]
    for i in range(index_from_my_string, len(chars)):
        new_string+=chars[i]
    print(new_string)


def problema7():
    my_function07('String!', 5)

"""Scrieți o funcție care primește ca parametru de intrare un șir și 
afișați șirul modificat prin inter-schimbarea celei de a doua și a penultimei litere din șir. Se consideră că șirul are lungimea minimă patru.
For example:
Test	Result
my_function('String!')
Sgrint!
"""


def makeAString(char_list):
    new_string=""
    for i in range(len(char_list)): new_string+=char_list[i]
    return new_string


def my_function08(my_string):
    chars = list(my_string)
    chars[len(chars)-2], chars[1]  = chars[1], chars[len(chars)-2]
    new_string = makeAString(chars)
    print(new_string)


def problema8():
    my_function08('String!')

"""
Scrieți o funcție care primește ca parametru de intrare un șir de caractere și afișați caracterele de pe pozițiile impare ale șirului.

For example:

Test	Result
my_function('String!')
Srn!

"""
def my_function09(my_string):
    chars = list(my_string)
    new_string=""
    for i in range(0, len(chars)):
        if i%2==0: new_string+=chars[i]
    print(new_string)

def problema9():
    my_function09('String!')


def my_function10(my_string):
    chars = list(my_string)
    new_string = ""
    for i in range(0, len(chars)):
        if i % 2 == 1: new_string += chars[i]
    print(new_string)


def problema10():
    my_function10('String!')
    # tig <--result aspected


def my_function11(my_string):
    char_list = list(my_string)
    # print(char_list)
    new_string=""
    for char in char_list:
        new_string+="".join(char).upper()
    print(new_string)


def problema11():
    my_function11('String!')


def my_function12(my_string):
    char_list = list(my_string)
    new_string = ""
    for char in char_list:
        new_string+="".join(char).lower()
    print(new_string)


def problema12():
    my_function12('String!')


def my_function13(my_string):
    char_list = list(my_string)
    new_string = ""
    for i in range(0, len(char_list)):
        if(i%3==2): new_string+=20*char_list[i]
    print(new_string)


def problema13():
    my_function13('String!')


def my_function14(my_str_de_cautat, my_str_de_gasit):
    char_de_cautat_list, char_de_gasit_list = list(my_str_de_cautat), list(my_str_de_gasit)
    poz=-1
    for i in range(0,len(char_de_cautat_list)):
        if len(char_de_cautat_list)>len(char_de_gasit_list)+i:
            for j in range(0, len(char_de_gasit_list)):
                if(char_de_cautat_list[i+j]==char_de_gasit_list[j]): poz=i
    new_string=""
    for i in range(0, poz):
        new_string+=char_de_cautat_list[i]
    print(new_string)


def problema14():
    my_function14('abababaa', 'ab')


def my_function15(my_string):
    char_list = list(my_string)
    new_string =  ""
    for i in range(0, len(char_list)):
        new_string+=char_list[len(char_list)-i-1]
    print(new_string)


def problema15():
    my_function15('abcd')


def my_function16(my_string):
    char_list = list(my_string)
    for i in range(0, len(char_list)-1):
        for j in range(i, len(char_list)):
            if(char_list[i] > char_list[j]): char_list[i], char_list[j]=char_list[j], char_list[i]
    new_string = ""
    for char in char_list: new_string+=char
    print(new_string)


def problema16():
    my_function16('dcbaa')


def my_function17(my_string):
    char_list = list(my_string)
    new_string=""
    # if '\t' in char_list: print("Exista tab!")
    for i in range(0, len(char_list)):
        if '\t' == char_list[i]: continue;
        new_string+=char_list[i]
    print(new_string)



def problema17():
    my_function17('Py\tCharm')


def my_function18(my_string):
    char_list = list(my_string)
    char_de_gasit_list=list("Mulțumesc")
    kounter = -1
    if len(char_list) >= len(char_de_gasit_list) :
        for i in range(0, len(char_de_gasit_list)):
            if (char_list[i] == char_de_gasit_list[i]):
                kounter +=1
    # print(kounter)
    if kounter==len(char_de_gasit_list)-1:
        print(True)
    else:
        print(False)
    new_string = ""



def problema18():
    my_function18('Mulțumesc frumos!')


def my_function19(my_string):
    char_list = list(my_string)
    new_string = ""
    gasit = False
    for char in char_list:
        if char == '\t' and gasit == False:
            new_string += '\n'
            gasit = True
        else:
            new_string += char
    print(new_string)


def problema19():
    my_function19('Mulțumesc\tfrumos!')


def my_function20(my_string1, my_string2):
    char_de_cautat_list=list(my_string1)
    char_de_gasit_list = list(my_string2)
    aparitii=0
    counter=0
    for i in range(0, len(char_de_cautat_list)):
        if len(char_de_cautat_list)>len(char_de_gasit_list)+i:
            for j in range(0, len(char_de_gasit_list)):
                if char_de_gasit_list[j]==char_de_cautat_list[i+j]: counter+=1
            if counter==len(char_de_gasit_list):
                aparitii+=1
            counter=0
    print(aparitii)


def problema20():
    my_function20('Python și PyCharm', 'Py')


def my_function21(my_string):
    list_of_strings = my_string.split(' ')
    new_string_list = []
    for i in range(0, len(list_of_strings)):
        new_string_list.append(list_of_strings[len(list_of_strings)-i-1])
    new_string=" ".join(new_string_list)
    print(new_string)



def problema21():
    my_function21('Python și PyCharm')


def my_function22(my_string):
    val = float(my_string)
    #print(val)
    dimension_cube = []
    volume = 1
    for i in range(0,3):
        dimension_cube.append(val)
    for i in range(0,3):
        volume*=dimension_cube[i]
    print(float(volume))
    # for i in range(0,len(char_list)):
    #     val_nr+=char_list[i]*p
    #     p/=10
    # print(val_nr)


def problema22():
    my_function22('2')


def my_function23(my_string, first_chars_from_str):
    char_list = list(my_string)
    new_string=""
    for i in range(0, len(char_list)):
        if i<first_chars_from_str: char_list[i]=char_list[i].lower()
        new_string+=char_list[i]
    print(new_string)


def problema23():
    my_function23('PYTHON', 2)


def my_function24(my_string, nr_of_chars_finished):
    char_list = list(my_string)
    for i in range(0, nr_of_chars_finished):
        char_list[-1-i]=char_list[-1-i].lower()
    new_string=""
    for char in char_list:
        new_string += char
    print(new_string)


def problema24():
    my_function24('MySQL', 3)


def my_function25(my_string, my_char):
    string_list = my_string.split(my_char)
    new_string=""
    poz_antepenultima=len(string_list)-3
    poz_penultima=len(string_list)-2
    for i in range(0,len(string_list)):
        if(i==poz_antepenultima):
            continue;
        if(i==poz_penultima):
            new_string+=string_list[poz_antepenultima]+string_list[poz_penultima]
            continue
        new_string+= " "+string_list[i]
    print(new_string)



def problema25():
    my_function25('Py thon PyCharm', ' ')


if __name__ == '__main__':
    #problema1()
    #problema2()
    #problema3()
    #problema4()
    # problema5()
    # problema6()
    # problema7()
    # problema8()
    # problema9()
    # problema10()
    # problema11()
    # problema12()
    # problema13()
    # problema14()
    # problema15()
    # problema16()
    # problema17()
    # problema18()
    # problema19()
    # problema20()
    # problema21()
    problema22()
    # problema23()
    # problema24()
    # problema25()