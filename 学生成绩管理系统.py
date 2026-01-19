class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display_info(self):
        return f'学生{self.name}的年龄为{self.age},成绩为{self.grade}'

class StudentManager:
    def __init__(self):
        self.students=[]
    def add(self,student):
        if student not in self.students:
            self.students.append(student)
            print(f'学生{student.name}添加成功')
        else:
            print(f'学生{student.name}已添加')
    def display_all(self):
        if not self.students:
            print('没有学生信息')
        for i,student in enumerate(self.students):
            print(f'{i}.{student.display_info()}')


if __name__ == "__main__":
    # 创建学生管理器
    manager = StudentManager()
    # 添加学生信息
    student1 = Student("张三", 18, 85)
    student2 = Student("李四", 19, 92)
    student3 = Student("王五", 17, 78)
    manager.add(student1)
    manager.add(student2)
    manager.add(student3)
    # 显示所有学生信息
    manager.display_all()
