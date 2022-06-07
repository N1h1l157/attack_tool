# coding=utf-8
# 创建新任务记录任务ID @get("/task/new")
# 设置任务ID扫描信息 @post("/option/<taskid>/set")
# 开始扫描对应的ID任务 @post("/scan/<taskid>/start")
# 读取扫描状态判断结果 @get("/scan/<taskid>/status")
# 获得到扫描结果 @get("/scan/<taskid>/data")
# 结束删除ID并获取结果 @get("/task/<taskid>/delete")

import time
import requests
import json


class sqlmapApi:
    url = ""
    headers = {
        'Content-Type': 'application/json'
    }
    data = ''
    res_id = ''

    def __init__(self, sql_url):
        self.sql_url = sql_url
        self.url = 'http://127.0.0.1:8775'
        self.data = {
            'url': self.sql_url,
        }

    def create_taskid(self):
        res = requests.get(self.url + "/task/new")  # 取到新任务的ID值
        # print(res.content.decode('utf-8'))
        if str(res.json()['success']) == 'True':
            self.res_id = res.json()['taskid']
            print('create id success: ' + self.res_id)
            self.set_taskid()
        else:
            print('create id failure!')

    def set_taskid(self):
        url_set = self.url + '/option/' + self.res_id + '/set'
        res_set = requests.post(url_set, data=json.dumps(self.data),
                                headers=self.headers)  # 设置任务ID扫描信息
        if str(res_set.json()['success']) == 'True':
            print('set id success: ' + self.res_id)
            print('now is test :' + self.sql_url)
            self.scan_taskid()
        else:
            print('set id failure: ' + self.res_id)

    def scan_taskid(self):
        url_scan = self.url + '/scan/' + self.res_id + '/start'
        res_scan = requests.post(url_scan, data=json.dumps(self.data),
                                 headers=self.headers)  # 开始扫描对应的ID任务
        if str(res_scan.json()['success']) == 'True':
            print('now is start scan url id: ' + self.sql_url + ' ' + self.res_id)
            self.status_taskid()
        else:
            print('scan id failure: ' + self.res_id)

    def status_taskid(self):
        url_status = self.url + '/scan/' + self.res_id + '/status'
        while 1:
            res_status = requests.get(url_status)  # 获得到扫描结果
            # print(res_status)
            if str(res_status.json()['status']) == 'running':
                # print(str(res_status.json()['status']))
                now_time = time.strftime("%m-%d %H:%M:%S", time.localtime())
                print("\033[0;31m [% s] \033[0m  now is scan id : " % now_time + self.res_id)
                time.sleep(0.5)
                pass
            else:
                self.data_taskid()
                break

    def data_taskid(self):
        url_data = self.url + '/scan/' + self.res_id + '/data'
        res_data = requests.get(url_data).content.decode('utf-8')  # 读取扫描状态判断结果
        # print('scan data is: ' + res_data)
        with open(r'scan_result.txt', 'a') as f:
            f.write(self.url + '\n')
            f.write(res_data + '\n')
            f.write('------------- Python by chentuo -------------------' + '\n')
            f.close()
        self.delete_taskid()

    def delete_taskid(self):
        url_delete = self.url + '/task/' + self.res_id + '/delete'
        res_delete = requests.get(url_delete)  # 结束删除ID并获取结果
        if str(res_delete.json()['success']) == 'True':
            print('now delete id success: ' + self.res_id)
            print('------------- next ---  next  ----------------' + '\n')


if __name__ == "__main__":
    for sqlurl in open('sqlurl.txt'):
        sqlurl = sqlurl.replace('\n', '')
        a = sqlmapApi(sqlurl)
        resq = requests.get(sqlurl)
        if resq.status_code != 200:
            print("un auth")
        else:
            a.create_taskid()
