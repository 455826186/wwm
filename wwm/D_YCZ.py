from wwmdqlb import login_1
from wwm import cz_tx
#提取测试用例保存到变量名all-case中
all_case=login_1()
print(all_case)
#提取第一条测试用例进行测试
print('第一条测试用例为：',all_case[0])
case_1=all_case[0]
ip="http://120.78.128.25:8766"
case_2 = cz_tx(ip + case_1[4], eval(case_1[5]))

for i in range(1,len(all_case)):
    text_case=all_case[i]
    token = case_2["data"]["token_info"]["token"]
    ip="http://120.78.128.25:8766"
    log_case=cz_tx(ip+text_case[4],eval(text_case[5]),"Bearer "+token)
    print('结果为:',log_case)


