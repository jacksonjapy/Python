# import time
# if __name__ == '__main__':
#     today = time.strftime("%A")
#     if today == "Monday" or today == "Wednesday" or today == "Friday":
#         print("今天公交出行!")
#     elif today == "Tuesday" or today == "Thursday":
#         print("今天打车出行！")
#     else:
#         print("今天共享单车出行")
import time
if __name__ == '__main__':
    today = time.strftime("%A")
    if today == "Monday" or today == "Wednesday":
        print("今天公交出行!")
    elif today == "Tuesday" or today == "Thursday":
        print("今天打车出行！")
    elif today == "Friday":
        print("开车出行！")
    else:
        print("今天共享单车出行")
