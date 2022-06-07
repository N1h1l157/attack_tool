# attack_tool

### 1.dirmap web目录扫描工具

https://github.com/H4ckForJob/dirmap

dirmap的安装指南

```git clone https://github.com/H4ckForJob/dirmap.git && 
cd dirmap
python3 -m pip install -r requirement.txt
python3 dirmap.py -i http://192.168.31.200 -lcf
```

dirmap的使用方法

```
python3 dirmap.py -i https://target.com -lcf
python3 dirmap.py -i 192.168.1.1 -lcf
python3 dirmap.py -i 192.168.1.0/24 -lcf
python3 dirmap.py -i 192.168.1.1-192.168.1.100 -lcf
python3 dirmap.py -iF targets.txt -lcf
```



### 2.子域名扫描

subdomainbrute与teemo的使用

```site:oldming.top -www
python subDomainsBrute.py oldming.top --full
python2 teemo.py --help
python2 teemo.py -d www.oldming.top
```



### 3.waf识别

shadon关键词搜索：X-Powered-By:WAF

```python main.py http://phw89.266933.com/```



### 4.EXP获取 POC

```
./searchsploit wordpress 4.1 搜索同时带有wordpress和4.1的漏洞
./searchsploit -s "wordpress 4.1" 更严格的搜索
./searchsploit "WordPress 4.1" -j 以json格式显示输出结果
./searchsploit "WordPress 4.1" -o 允许标题溢出其列
./searchsploit "WordPress 4.1" -p 显示漏洞的完整地址
./searchsploit "WordPress 4.1" -w 显示网络地址而非本地地址
./searchsploit "WordPress 4.1" -u 更新检查并安装任何数据库包更新
./searchexploit wordpress -c 区分大小写搜索
./searchsploit "Landa Driving School Management System 2.0.1 - Arbitrary File Upload" 
```



#### 5.pocsuite3获取poc

```
cd pocsuite && python cli.py -h
```

