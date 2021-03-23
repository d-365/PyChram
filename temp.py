# 普通同步代码实现多个IO任务
import time
import threading


def taskIO_1():
    print('开始运行IO任务1...')
    time.sleep(3)  # 假设该任务耗时3s
    print('IO任务1已完成，耗时3s')


def taskIO_2():
    print('开始运行IO任务2...')
    time.sleep(3)  # 假设该任务耗时3s
    print('IO任务2已完成，耗时3s')


if __name__ == "__main__":
    start = time.time()
    t1 = threading.Thread(target=taskIO_1)
    t2 = threading.Thread(target=taskIO_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # taskIO_1()
    #     # taskIO_2()
    print('所有IO任务总耗时%.5f秒' % float(time.time() - start))
