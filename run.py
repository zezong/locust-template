#-*- coding: UTF-8 -*-
#
#	执行压力测试
#	python 3
#
import os

if __name__ == '__main__':
	os.system('locust -f locustfile.py --no-web -c20 -r20 -t10s --csv=example --loglevel=INFO --logfile=test.log --host=https://lottery.618sale.com')
	# -f       指定配置文件
	# --no-web 不开启WEB UI; -c指定要生成的用户数; -r指定孵化率(每秒要生成的用户数); --no-web与-c和-r一起使用
	# -t       指定测试的运行时间
	# --csv    保存统计信息的文件，会命令为example_distribution.csv和example_requests.csv
	# --host   压力测试的网址