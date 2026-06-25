tasks = {
    "Do dishes": "Incomplete",
    "Do the course": "Incomplete",
    "Do laundry": "Complete",
}
list_tasks = list(tasks)
Incomplete_tasks = []
Complete_tasks = []
# input_list=[]


def add_tasks():
    is_true2 = True
    while is_true2:
        new_task = input("\t\tEnter The task: ")
        new_status = input("\t\tEnter the staus: ")
        if new_status in ["Complete", "complete", "Incomplete", "incomplete"]:
            tasks[new_task] = new_status
            is_true2 = False
        else:
            print("\t\t\tType complete or incomplete")


def mark_complete():

    is_true = True
    while is_true:
        task_to_remove = int(
            input("\t\tWhat tasks would you like to remove its s.no: ")
        )
        if 0 < task_to_remove <= len(list_tasks):
            task_to_be_marked = list_tasks[task_to_remove - 1]
            tasks[task_to_be_marked] = "Complete"
            print(tasks)
            is_true = False
        else:
            print("\t\tInvalid input")


def mark_incomplete():
    is_true = True
    while is_true:
        task_to_remove = int(
            input("\t\tWhat tasks would you like to mark incomplete: ")
        )
        if 0 < task_to_remove <= len(list_tasks):
            task_to_be_marked = list_tasks[task_to_remove - 1]
            tasks[task_to_be_marked] = "Incomplete"
            print(tasks)
            is_true = False
        else:
            print("\t\tInvalid input")


def get_items():
    print("\t\tYou Tasks Are:")
    for n, (task, status) in enumerate(tasks.items()):
        print(f"\t\t{n + 1}. {task}: {status})")


def get_complete():
    Complete_tasks.clear()
    for n, (task, status) in enumerate(tasks.items()):
        if status == "Complete":
            Complete_tasks.append(task)
    return Complete_tasks


def get_incomplete():
    Incomplete_tasks.clear()
    for task, status in tasks.items():
        if status == "Incomplete":
            Incomplete_tasks.append(task)
    return Incomplete_tasks


def reemove_task():
    remove_input = input("\t\tEnter the task to remove: ")
    remove_input1 = remove_input.split()
    remove_list = [int(i) for i in remove_input1]
    for j in remove_list:
        rem_item = list_tasks[j - 1]
        tasks.pop(rem_item)
    return tasks


a = get_incomplete()
is_true = True
while is_true:
    print("\n\t\tWelcome To the  To Do list App")
    print("\t\tWhat tasks would you like to perfom?")
    print("\t\t1.Review the To Do list")
    print("\t\t2.Mark tasks as Complete")
    print("\t\t3.Mark tasks as Incomplete")
    print("\t\t4.review the completed tasks")
    print("\t\t5.review the incomplete taks")
    print("\t\t6.Remove a task ")
    print("\t\t7.Add a task ")
    print("\t\t8.Exit")
    user_input = int(input("\t\tEnter the Choice(1-6): "))
    if user_input == 1:
        get_items()
    elif user_input == 2:
        mark_complete()
    elif user_input == 3:
        mark_incomplete()
    elif user_input == 4:
        print(get_complete())
    elif user_input == 5:
        print(get_incomplete())
    elif user_input == 6:
        c = reemove_task()
        print(c)
    elif user_input == 7:
        add_tasks()
    elif user_input == 8:
        print("\t\tThank You for Using the Program")
        is_true = False
    else:
        print("\t\t\tinvalid Choice")
# class CustomeError(Exception):
#     print("HI")
# age=-4
# try:
#     if age <0:
#         raise CustomeError()
# except CustomeError as e:
#     print(e)
# count=[]
# numbers_list=[]


# def compassionate_counter(num_children, special_number):
#     count = []  # result list
#     count1 = 0  # running total of divisible numbers
#     for number in range(1, num_children + 1):
#         if number % special_number == 0:
#             count1 += 1
#         count.append(count1)
#     return count


# a = compassionate_counter(5, 2)
# # print("hi")
# print(a)
