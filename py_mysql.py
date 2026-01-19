# import pymysql
#
# def main():
#     conn=pymysql.connect(
#         host='localhost',#数据库地址
#         user='root',
#         password='123456',
#         database='test3',
#         charset='utf8'
#     )
#     #创建游标对象
#     cursor=conn.cursor()
#     print('数据库连接成功')
#     #创建学生表
#     # sql="""create table students(
#     #     id int primary key auto_increment comment '自增主键',
#     #     name varchar(50) not null comment '姓名',
#     #     age int not null comment '年龄',
#     #     sex varchar(50) comment '性别'
#     # );
#     #     """
#     #插入单条数据
#     # insert_sql_2=('insert into students(name,age,sex) values(%s,%s,%s);')
#     # data=[  ('王芳', 32, '女'),
#     #         ('刘伟', 19, '男'),
#     #         ('陈静', 28, '女'),
#     #         ('赵磊', 45, '男'),
#     #         ('孙悦', 22, '女'),
#     #         ('周明', 36, '男'),
#     #         ('吴琳', 29, '女'),
#     #         ('郑浩', 41, '男'),
#     #         ('高婷', 26, '女')]
#
#     #多条数据插入
#     # cursor.executemany(insert_sql_2,data)
#     # for i in data:
#     #     cursor.execute(insert_sql_2,i)
#
#     # cursor.execute('select * from test3.students')
#     # data=cursor.fetchall()
#     # print('查询所有信息')
#     # for i in data:
#     #     print(i)
#     #
#     # print('-----------------------------')
#     # print('查询年龄大于20岁的男性，按年龄大小降序排列')
#     # cursor.execute("""select * from test3.students where age>20 and sex='男' order by age desc""")
#     # data_2=cursor.fetchall()
#     # for j in data_2:
#     #     print(j)
#     #
#     # conn.commit()
#     # conn.close()
#     # cursor.execute("""
#     # update test3.students set sex='girl' where sex='女'
#     # """)
#     # print(f'受影响的行数{cursor.rowcount}')
#
#
#     cursor.execute(
#         """
#         delete from test3.students where age<30
#         """
#     )
#     print(f'受影响的行数为{cursor.rowcount}')
#     conn.rollback()
#     print(f'受影响的行数为{cursor.rowcount}')
#
#
#     # print('-----------------')
#     # cursor.execute("""
#     # alter table test3.students rename column sex to gender
#     # """)
#     # conn.commit()
#     conn.close()
#
#
#
#
# if __name__=='__main__':
#     main()


import pymysql
def main():
    conn=pymysql.connect(host='localhost',
                         user='root',
                         database='test2',
                         password='123456',
                         charset='utf8'
                         )

    cursor=conn.cursor()
    try:
        cursor.execute("""
        create table company(
        id int primary key auto_increment comment '编号',
        name varchar(25) not null comment '姓名',
        department varchar(100) comment '部门',
        salary float comment '工资')
        """)
        print('创建成功')
    except Exception as e:
        print(f'表创建数百：{e}')

    try:
    #批量插入数据
        print('批量插入数据')
        data=[
            ('张三','销售部',8000),
            ('李四', '技术部',10000),
            ('王五', '人事部',7500)
        ]
        # insert_sql=("""
        # # insert into test2.company (name,department,salary) values()
        # # """))
        cursor.executemany("""
        insert into test2.company (name,department,salary) values(%s,%s,%s)
        """,data)
        print('数据插入成功')
        conn.commit()
    except Exception as e:
        print(f'数据插入失败：{e}')

    try:
    #查询所有信息
        print('查询所有信息')
        cursor.execute("""select * from test2.company""")
        data=cursor.fetchall()
        for i in data:
            print(i)
        conn.commit()
    except Exception as e:
        print(f'查询失败：{e}')

    try:
    #更新张三的工资
        cursor.execute("""update test2.company set salary=8500 where name='张三'""")
        print('更新成功')
        conn.commit()
    except Exception as e:
        print(f'更新失败：{e}')

    try:
    #删除王五的记录
        print('删除王五数据')
        cursor.execute("""delete from test2.company where name='王五'""")
        print('删除成功')
        conn.commit()
    except Exception as e:
        print(f'删除失败:{e}')

    conn.close()




if __name__=='__main__':
    main()