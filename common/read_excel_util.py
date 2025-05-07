import pandas
#读取Excel文件，以列表的形式输出
def read_excel_to_login(excel_path,sheet_name):
    data=pandas.read_excel(excel_path,sheet_name,engine='openpyxl')
    dict_list=data.to_dict(orient='records')
    return dict_list

# if __name__ == '__main__':
#     read_excel_to_login(r"C:\Program Files\pycharmproject\testcases01\login_caseinfo.xlsx","单据信息")