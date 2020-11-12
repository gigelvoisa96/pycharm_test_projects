def my_function(my_string):
    char_list = list(my_string)
    new_string = ""
    repeat_string=""
    nr_of_repeat=0
    for i in range(0, len(char_list)):
        if(i%3==2):
            repeat_string+=char_list[i]
            nr_of_repeat+=1
    # for i in range(0, nr_of_repeat):
    new_string=20*repeat_string+"\n"
    print(new_string)
my_function('abc')
