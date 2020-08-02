"""
============================
Author:柠檬班-木森
Time:2020/7/30   21:50
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import openpyxl


class Excel:
    def __init__(self, filename, sheet_name):
        self.filename = filename
        self.sheet_name = sheet_name

    def open(self):
        # 第一步：将excel文件加载到一个工作簿对象中
        self.wb = openpyxl.load_workbook(self.filename)
        # 第二步：选择文件中的表单
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        """读数据"""
        self.open()
        res = list(self.sh.rows)
        # 获取第一行表头数据
        title = [c.value for c in res[0]]
        cases_data = []
        # 遍历除第一行之外所有的行
        for row in res[1:]:
            # 获取遍历出来这一行的数据
            data = [c.value for c in row]
            # 和表头打包成字典
            case = dict(zip(title, data))
            cases_data.append(case)
        return cases_data

    def write_data(self, row, column, value):
        """写数据"""
        self.open()
        self.sh.cell(row=row, column=column, value=value)
        self.wb.save(self.filename)


if __name__ == '__main__':
    excel = Excel("cases.xlsx", "register")
    escel2 =Excel("cases.xlsx", "login")
    data = excel.read_data()
    print(data)
