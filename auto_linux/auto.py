import paramiko
"""
自动化实现对远程服务器的操作
"""

# 创建sshclient实例对象
ssh = paramiko.SSHClient()
# 信任远程机器，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接远程机器 地址 端口 用户名 密码
ssh.connect("192.168.199.152", 22, "root", "123456")

ssh.exec_command('cd /home/tmp;mkdir demo')

# 获得执行命令返回值
stdin, stdout, stderr = ssh.exec_command('ps -ef|grep docker|grep -v grep')
output = stdout.read().decode()
print(output)

parts = output.split('\n')
num = []
for part in parts:
    if part:
        fileds = part.split(' ')
        fileds = [filed for filed in fileds if filed]
        num.append(fileds[1])
print(num)

# 上传文件到远程服务器
sftp = ssh.open_sftp()
# sftp.put(r'本机文件路径', '服务器路径')
sftp.close()

#
