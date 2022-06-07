import base64
import os

# 解密JAVA序列化后并且加密后的代码，此处先base64解密，在hex转换，最后反序列化
# 若要将其他的序列化并加密的java代码破解，需要放在/Users/chentuo/Public/shentou/payload/目录下
# 并且将代码中 rebound_shell_payload.txt 替换为自己浏览的对方的java代码中敏感信息的文件
with open('/Users/chentuo/Public/tool/java_serial_序列化漏洞/payload/rebound_shell_payload.txt', 'rb') as rebound_shell_payload:
    decode_payload = base64.b64decode(rebound_shell_payload.read())
with open('/Users/chentuo/Public/tool/java_serial_序列化漏洞/payload/decode_source_json_hex.txt', 'w') as decode_payload_hex:
    decode_payload_hex.write(decode_payload.hex())
# 决定是否生成ace开头的十六进制代码
decode_deserialization = os.popen(
    "java -jar /Users/chentuo/Public/tool/java_serial_序列化漏洞/SerializationDumper/SerializationDumper.jar -f /Users/chentuo/Public/tool/java_serial_序列化漏洞/payload/decode_source_json_hex.txt").read()
with open('/Users/chentuo/Public/tool/java_serial_序列化漏洞/payload/decode_finally.txt', 'w') as deserialization_file:
    deserialization_file.write(decode_deserialization)
print(decode_deserialization)

# 需要拿到对方输入的java序列化后的已经加密后文件 这里以 rebound_shell_payload.txt举例
# -> decode_source_json_hex.txt 先是以hex的形式保存
# -> decode_finally.txt  再以反序列化的形式保存

