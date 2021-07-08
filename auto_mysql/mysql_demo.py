import pymysql
"""
自动化操作数据库
"""
conn = pymysql.connect(
    host="192.168.199.152",
    port=3310,
    user="root",
    password="123456",
    db="mydb",
    charset="utf8"
)
# 创建游标对象
cur = conn.cursor()

# for i in range(cur.rowcount):
#     row = cur.fetchone()
#     if row[1] == '李四':
#         print(f"检查点=>> 学生{row[1]}找到，通过")
#         break
# for i in range(1000):
#     cur.execute(f"INSERT INTO `student`(`name`,`pwd`,`sex`) VALUES('赵四_{i + 1}','abcde','男');")
# conn.commit()

cur.execute('select * from student;')
for i in range(cur.rowcount):
    row = cur.fetchone()
    print(row)
conn.close()
