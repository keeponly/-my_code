"""actionChains 原理练习。"""


def move_to_element():
    print('running')

def click():
    print('eating')

def context_click():
    print('movie')


my_list = []

my_list.append(move_to_element)

my_list.append(click)

my_list.append(context_click)

def perfom(my_list):
    for i in my_list:
        i()

perfom(my_list)