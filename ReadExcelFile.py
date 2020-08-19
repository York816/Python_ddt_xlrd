import xlrd


def readxls():
    xl = xlrd.open_workbook(r'C:\PycharmProjects\Python_ddt_xlrd\pytestfile.xlsx', encoding_override="utf-8")
    sheet1 = xl.sheet_by_name('Sheet1')  # 指定表1
    allrows = sheet1.nrows
    # print(get_allrows)
    listdata = []  # 定义空列表，用来存放读取出来的每行数据
    for i in range(1, allrows):  # 循环读取所有行（忽略首行表头信息）
        j = sheet1.row_values(i, 0, 2)  # 读取第i行的第0~2列（不含第2列） 或 直接将每一行的值插入list
        # listdata.append(sheet1.row_values(i)) # 直接将每一行的值插入list
        listdata.append(j)  # 读一行追加一行存入listdata中
    return listdata  # 返回列表


if __name__ == '__main__':
    print(readxls())
