import requests
from lxml import etree
import base64
import re
import time
import base
import config
from urllib.parse import quote, unquote


def spider():
    searchbs64 = quote(str(base64.b64encode(config.SearchKEY.encode()), encoding='utf-8'))

    headers = {
        'cookie': 'refresh_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTQ0NTA4LCJtaWQiOjEwMDA4NTEzOSwidXNlcm5hbWUiOiJnaXRmbHV0dGVyU3R1ZGVudCIsImV4cCI6MTY0NTMzNTY2MCwiaXNzIjoicmVmcmVzaCJ9.NrplRTX8XmBcYNcyhaSXSc6VLom5Nw1bR1brePaYBGO2AVGawK0YV8ssln1q8Rm6jM3RFhoozus_Pxzp5aesvg; isUpgrade=; befor_router=; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTQ0NTA4LCJtaWQiOjEwMDA4NTEzOSwidXNlcm5hbWUiOiJnaXRmbHV0dGVyU3R1ZGVudCIsImV4cCI6MTY0NTMyMTEyNy42Mzc4NzIyLCJpc3MiOiJyZWZyZXNoIn0.uepsL7hdNknmnxIzNbDCaBDelVMQEnRcnYuYakRKRkfZAYKn0dWGcG225zHJ762K1i0qK8TmzPJX5cFZFuN-ag; user=%7B%22id%22%3A144508%2C%22mid%22%3A100085139%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22gitflutterStudent%22%2C%22nickname%22%3A%22gitflutterStudent%22%2C%22email%22%3A%221228057869%40qq.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22key%22%3A%22c8ba2b37e5c2b24e196940b4c1244637%22%2C%22rank_name%22%3A%22%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7%22%2C%22rank_level%22%3A0%2C%22company_name%22%3A%22gitflutterStudent%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22credits%22%3A132%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%7D'
        # 'cookie' : 'cookie: isUpgrade=; befor_router=; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTQ0NTA4LCJtaWQiOjEwMDA4NTEzOSwidXNlcm5hbWUiOiJnaXRmbHV0dGVyU3R1ZGVudCIsImV4cCI6MTY0NTExOTY2MH0.VrC4uHyBWz_C31v6spAHm07u-hKXOvZjUkOIStKkxXkpOweZVqty7pvzirRRxaAZwaIZ8qYziVQpO_BKNhVTNg; refresh_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTQ0NTA4LCJtaWQiOjEwMDA4NTEzOSwidXNlcm5hbWUiOiJnaXRmbHV0dGVyU3R1ZGVudCIsImV4cCI6MTY0NTMzNTY2MCwiaXNzIjoicmVmcmVzaCJ9.NrplRTX8XmBcYNcyhaSXSc6VLom5Nw1bR1brePaYBGO2AVGawK0YV8ssln1q8Rm6jM3RFhoozus_Pxzp5aesvg; user=%7B%22id%22%3A144508%2C%22mid%22%3A100085139%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22gitflutterStudent%22%2C%22nickname%22%3A%22gitflutterStudent%22%2C%22email%22%3A%221228057869%40qq.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22key%22%3A%22c8ba2b37e5c2b24e196940b4c1244637%22%2C%22rank_name%22%3A%22%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7%22%2C%22rank_level%22%3A0%2C%22company_name%22%3A%22gitflutterStudent%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22credits%22%3A78%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%7D'
    }
    print("爬取页面为:https://fofa.info/result?&qbase64=" + searchbs64)
    html = requests.get(url="https://fofa.info/result?&qbase64=" + searchbs64, headers=headers).text
    tree = etree.HTML(html)
    # print(tree)
    try:
        pagenum = tree.xpath('//li[@class="number"]/text()')[-1]
    except Exception as e:
        print(e)
        pagenum = '0'
        pass
    # pagenum = re.findall('>(\d*)</a> <a class="next_page" rel="next"', html)
    print("该关键字存在页码: " + pagenum)
    print("爬取页数默认为5页，如果有需要，请在base.py文件中修改")
    # config.StartPage=input("请输入开始页码: ")
    # config.StopPage=input("请输入终止页码: ")
    doc = open("%s.txt" % config.SearchKEY, "a+")
    for i in range(int(config.StartPage), int(config.StopPage) + 1):
        # print("Now write " + str(i) + " page")
        url = "https://fofa.info/result?page=" + str(i) + "&page_size=10&qbase64=" + searchbs64

        now_time = time.strftime("%m-%d %H:%M:%S", time.localtime())
        print("\033[0;31m [% s] \033[0m" % now_time + "  " + url)

        # print(url)
        try:
            # print('fetching page :' + str(i))
            url_source = requests.get(url, headers=headers).content.decode('utf-8')  # 拿到返回的源码
            html = etree.HTML(url_source)  # 利用etree.HTML把字符串解析成HTML文档
            ip_data1 = html.xpath('//span[@class="aSpan"]/a[@target="_blank"]/@href')  # 拿到href的数据
            ip_data1 = '\n'.join(ip_data1)  # 爬取到每两个数据之间都要进行换行
            print(ip_data1)
            print('------------------------------------------------------------------------')
            ip_data2 = html.xpath('//span[@class="aSpan"]/text()')  # 拿到href的数据
            ip_data2 = '\n'.join(ip_data2)
            print(ip_data2)

            ip_data = ip_data1 + ip_data2
            doc.write(ip_data + '\n')  # 加'\n'是为了下一次写入的时候另起一行

        except Exception as e:
            pass
        time.sleep(config.TimeSleep)
    doc.close()
    print("OK,Spider is End .")


def main():
    base.logo()
    base.checkSession()
    base.init()
    spider()


if __name__ == '__main__':
    main()
