import random

def check_loops(a_list):
    for item in a_list:
        print(item)

def learn_about_range(n_iterations):
    sum_of_numbers = 0
    for i in range(n_iterations):
        print(f"Iteration {i}")
        # sum_of_numbers + 1 = 1
        # sum_of_numbers + 2 = 1 + 2 =3
        # sum_of_numbers + 3 = 1 + 2 + 3 = 6
        sum_of_numbers += i # sum_of_numbers = sum_of_numbers + i

    print(f"Sum of numbers: {sum_of_numbers}")

def learn_about_steps_range(n_iterations):
    sum_of_numbers = 0
    for i in range(n_iterations, 0, -3):
        print(f"Iteration {i}")
        sum_of_numbers += i

    print(f"Sum of numbers: {sum_of_numbers}")


def learn_about_while_loop(n_iterations):
    sum_of_numbers = 0
    i = 0
    while i < n_iterations:
        print(f"Iteration {i}")
        sum_of_numbers += i
        i += 1

    print(f"Sum of numbers: {sum_of_numbers}")


if __name__ == '__main__':

    temp_list = []
    # print(temp_list)

    temp_list.append(1)
    # print(temp_list)

    temp_list.append(2)
    # print(temp_list)

    temp_list.append("Ladi")    
    # print(temp_list)

    # check_loops(a_list = temp_list) # [1,2,'ladi']

    # learn_about_range(10)

    # learn_about_steps_range(10)

    # random_list_100 = [random.randint(0, 100) for i in range(100)]
    # print(random_list_100)
    # print(105 not in random_list_100)

    # text = "camel"
    # print(text)
    # print([ch for ch in text])    

    # for ch in text:
    #     print(ch)
    n_iter = int(input("How many iterations? "))
    learn_about_while_loop(n_iter)
