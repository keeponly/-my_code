# @Time     :2020/10/15  10:08
# @Author   :wang-kai
# @tel      :15313929271
# @File    :队列.py

# 创建一个队列  3 代表里面的里面最多3个任务 任务就是队列里面的数据
from queue import Queue

q = Queue(10)
# 队列增加数据
q.put(2)
# 获取队列数据
print(q.get())

print(q.qsize())  # 0 因为放进去一个数据,但是有取出来一个数据,所以最后是0
# # 在完成一项工作后,使用该方法像队列发送信号,表示该任务执行完毕
# q.task_done()
# # 任务中队列是否执行完毕
# q.join()

