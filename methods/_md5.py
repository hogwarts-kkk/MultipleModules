import hashlib


def get_md5(_passwd):
    """ md5 加密函数
    :param _passwd:传入的密码
    :return: md5加密后密码
    """
    # 实例化一个md5对象
    md5 = hashlib.md5()
    # 调用加密方法 进行加密
    md5.update(_passwd.encode("utf-8"))
    # 返回加密后的密码
    return md5.hexdigest()


if __name__ == '__main__':
    a = get_md5("123456")
    print(a)
