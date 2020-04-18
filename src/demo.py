from time import sleep
from threading import Thread, current_thread


def work_process(task_num):
    for i in range(task_num):
        print(current_thread().name, i)
        sleep(1)


def thread_task():
    print('Launch task', current_thread().name)
    work_process(100)


if __name__ == '__main__':
    for i in range(3):
        Thread(name='thread' + str(i), target=thread_task).start()
    # work_process(300)

