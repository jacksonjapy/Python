class Teacher():
    def __init__(self, course_id, course_name, course_teacher, course_semester):
        self.course_id = course_id
        self.course_name = course_name
        self.course_teacher = course_teacher
        self.course_semester = course_semester
        self.total_course = 0

    def show_course(self):
        print("课程编号：%s" % self.course_id)
        print("课程名称：%s" % self.course_name)
        print("课程教师：%s" % self.course_teacher)
        print("课程学期：%s" % self.course_semester)
        print("课程总人数：%s" % self.total_course)
        print(self.total_course)


if __name__ == '__main__':
    zhangsan = Teacher("001", "python", "张三", "2019-2020")
    zhangsan.show_course()
    zhangsan.total_course = 100
    zhangsan.show_course()
    print(zhangsan.total_course)
    lisi = Teacher("002", "java", "李四", "2019-2020")
    lisi.show_course()
    print(lisi.total_course)
