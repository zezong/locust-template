#-*- coding: UTF-8 -*-
#
#   压力测试配置文件
#
import logging
from locust import HttpLocust, TaskSet, task

#去除警告用的，https下面使用的是verify=False
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class WebsitTasks(TaskSet):
    def on_start(self): # 初始化工作，每个locust用户开始做的第一件事
        logging.info('--- User Start ---')

    @task(1) # 这个装饰器的意思是：给每个人物设置权重，比如这个函数执行的权重就是1，如果下面是2，那么下面的函数就会更多的被执行
    def enter_classroom(self):
        with self.client.get('/test', catch_response=True, verify=False) as response:
            if response.status_code == 200:
                response.success()
                print('-' * 50)
                logging.info('返回值状态码为：%s' % response.status_code)
                print('-' * 50)
            else:
                print('*' * 50)
                response.failure('GetActConfig[Failed!]')
                logging.error('错误请求，状态码为：', response.status_code)
                print('*' * 50)

class WebsiteUser(HttpLocust):
    host = 'https://lottery.618sale.com' # 被压测系统的host,在终端中启动locust时没有指定--host参数时才会用到

    task_set = WebsitTasks # TaskSet类，该类定义用户人物信息，必填，这里就是：WebsiteTasks类名，因为该类集成TaskSet
    min_wait = 0 # 每个用户执行两个任务间隔时间的上下限(毫秒)，具体数据在上下限中随机取值，若不指定：默认间隔时间固定为1秒
    max_wait = 0