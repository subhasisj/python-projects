def check_loops(a_list):
    for item in a_list:
        print(item)

if __name__ == '__main__':

    temp_list = []
    # print(temp_list)

    temp_list.append(1)
    # print(temp_list)

    temp_list.append(2)
    # print(temp_list)

    temp_list.append("Ladi")    
    # print(temp_list)

    check_loops(a_list = temp_list) # [1,2,'ladi']

    
        # check_loops()