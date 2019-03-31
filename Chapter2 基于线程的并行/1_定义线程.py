import threading


def function(idx):
    for _ in range(5):
        print('Function called by thread {}'.format(idx))


threads = []
for i in range(10):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)

for t in threads:
    # 调用start使线程开始运行
    t.start()

for t in threads:
    # join会阻塞调用该方法的线程
    # 在这里的意思就是只有t执行完了, 主线程才会执行
    t.join()

print('Done')
