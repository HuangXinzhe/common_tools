import os
import xlsxwriter as xw
import pandas as pd
from multiprocessing import Process
import re


def file_name(file_dir):
    # for root, dirs, files in os.walk(file_dir):
    #     print(root) # 当前目录路径
    #     print(dirs) # 当前路径下所有子目录
    #     print(files) # 当前路径下所有非目录子文件
    for root, dirs, files in os.walk(file_dir):
        return files


table_title = ['index_id', 'positionName', 'salary', 'companySize', 'workYear', 'education', 'companyShortName',
               'positionUrl', 'createTime', 'companyLabelList', 'positionDetail', 'companyFullName', 'financeStage',
               'industryField', 'positionAddress', 'positionType', 'positionSource', 'city', 'searchWord', 'tags']


def write_to_excel(file_li, f_name):
    # f_name = f"/Users/tanxinkeji/Documents/xiaobo/data/jd_data2.xlsx"
    # f_name = f"jd_data2.xlsx"
    workbook = xw.Workbook(f_name)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    worksheet1.write_row(0, 0, table_title)  # 从A1单元格开始写入表头
    for i, f_ in enumerate(file_li):
        df = pd.read_excel(f'/Users/tanxinkeji/Documents/xiaobo/data/jd_data/{f_}')  # 读取xlsx中第一个sheet
        val = df.columns.values
        new_v = []
        for vv in val:
            if not vv:
                vv = 'none'
            new_v.append(vv)
        worksheet1.write_row(i + 1, 0, new_v)  # 从A1单元格开始写入表头
        if i % 500 == 0:
            print(i)
    workbook.close()
    # workbook.close()


def get_library(col, f):
    a = set()
    for i in range(14):
        print(i)
        df = pd.read_excel(f'jd_data_{i}.xlsx')
        a |= set(df[col].values)
    print(len(a))
    fw = open(f, 'w')
    for i in a:
        fw.write(str(i) + '\n')
    fw.close()


def get_company_industry():
    a = {}
    for i in range(14):
        print(i)
        df = pd.read_excel(f'/Users/tanxinkeji/Documents/xiaobo/data/jd_data_{i}.xlsx')
        # df = pd.read_excel(f'/Users/tanxinkeji/Documents/xiaobo/data/jd_data_test.xlsx', )
        companyShortName = df['companyShortName'].values
        industryField = df['industryField'].values
        for j in range(len(companyShortName)):
            if 'none' not in industryField[j]:
                if not a.get('companyShortName', ''):
                    a[companyShortName[j]] = industryField[j]
    fw = open(f'../data/words_dictionary/company/company_industry.txt', 'w')
    for i in a:
        tem_li = [i, a[i]]
        fw.write('\t'.join(tem_li) + '\n')
    fw.close()


def mul_pro_write_excel():
    file_li = file_name(f'/Users/tanxinkeji/Documents/xiaobo/data/jd_data')
    # write_to_excel(file_li)
    # get_library()
    len_file_li = len(file_li)
    each_step = 50000
    p_li = []
    for i in range(int(len_file_li / each_step) + 1):
        tem_file_li = file_li[i * each_step:(i + 1) * each_step]
        print(len(tem_file_li))
        p = Process(target=write_to_excel, args=(tem_file_li, f"jd_data_{i}.xlsx",))
        p_li.append(p)
    for p in p_li:
        p.start()
    for p in p_li:
        p.join()


def mul_pro_gen_library():
    p_li = []
    # p = Process(target=get_library, args=('companyShortName', f'../resume_project/data/company/company2.txt',))
    # p_li.append(p)
    # p = Process(target=get_library, args=('positionName', f'../resume_project/data/job/job2.txt',))
    # p_li.append(p)
    # p = Process(target=get_library, args=('companyLabelList', f'../resume_project/data/welfare/welfare.txt',))
    # p_li.append(p)
    # p = Process(target=get_library, args=('industryField', f'../resume_project/data/industry/industry.txt',))
    # p_li.append(p)

    for p in p_li:
        p.start()
    for p in p_li:
        p.join()


def process_industry():
    fr = open(f'../resume_project/data/industry/industry.txt')
    a = set()
    for line in fr:
        line = line.strip()
        if re.findall(r'.*([0-9]).*', line):
            continue
        if line:
            raw_li = re.split('[,，|｜/(.)丨、 ]', line)
            if raw_li:
                for i in raw_li:
                    if len(i) > 1:
                        a.add(i.strip())
    print(len(a))
    fr.close()
    fw = open(f'../resume_project/data/industry/industry2.txt', 'w')
    for i in a:
        fw.write(str(i) + '\n')
    fw.close()


def process_welfare():
    fr = open(f'../resume_project/data/welfare/welfare.txt')
    a = set()
    for line in fr:
        if line.strip():
            if ', ' in line.strip():
                l = line.strip().split(', ')
            elif ',' in line.strip():
                l = line.strip().split(',')
            else:
                l = line.strip().split('，')
            for i in l:
                if i.strip():
                    a.add(i)
    print(len(a))
    fw = open(f'../resume_project/data/welfare/welfare2.txt', 'w')
    for i in a:
        fw.write(str(i) + '\n')
    fw.close()


def process_company():
    fr = open(f'../resume_project/data/company/company2.txt')
    res = set()
    for line in fr:
        if line.strip():
            flag = 0
            # line = '汇云聚美(苏州)生物科技'
            line = line.strip()
            if "某" in line or "知名企业" in line or 'xx' in line or 'XX' in line or '***' in line:
                continue
            if '...' in line:
                line = line.replace('...', '')
            if '.1' in line:
                line = line.replace('.1', '')
            if '-' in line:
                for i in line.split('-'):
                    res.add(i)
            if '(' not in line and ')' not in line and '（' not in line and '）' not in line:
                res.add(line)
            else:
                flag = 1
                if '(' in line and ')' in line:
                    rep_s = re.findall(r'.*(\(.*\)).*', line)
                    if rep_s:
                        if len(rep_s) >= 2:
                            print(rep_s)
                        new_line = line.replace(rep_s[0], '')
                        if new_line:
                            res.add(new_line)
                if '（' in line and '）' in line:
                    rep_s = re.findall(r'.*(（.*）).*', line)
                    if rep_s:
                        new_line = line.replace(rep_s[0], '')
                        if new_line:
                            res.add(new_line)
            if flag:
                if '发展有限公司' in new_line:
                    new_line2 = new_line.replace('发展有限公司', '')
                    if new_line2:
                        res.add(new_line2)
                elif '股份有限公司' in new_line:
                    new_line2 = new_line.replace('股份有限公司', '')
                    if new_line2:
                        res.add(new_line2)
                elif '有限公司' in new_line:
                    new_line2 = new_line.replace('有限公司', '')
                    if new_line2:
                        res.add(new_line2)
            else:
                if '发展有限公司' in line:
                    new_line = line.replace('发展有限公司', '')
                    if new_line:
                        res.add(new_line)
                elif '股份有限公司' in line:
                    new_line = line.replace('股份有限公司', '')
                    if new_line:
                        res.add(new_line)
                elif '有限公司' in line:
                    new_line = line.replace('有限公司', '')
                    if new_line:
                        res.add(new_line)
    print(len(res))
    fr.close()
    fw = open(f'../resume_project/data/company/company3.txt', 'w')
    for i in res:
        fw.write(str(i) + '\n')
    fw.close()


def process_job():
    fr = open(f'../resume_project/data/job/job2.txt')
    res = set()
    for line in fr:
        if line.strip():
            line = line.strip()
            # 第一步 去除_x000D_
            if '_x000D_' in line:
                line = line.replace('_x000D_', '').strip()
            # 第二步 去除括号
            if '(' in line or ')' in line or '（' in line or '）' in line:
                rep_s = re.findall(r'.*?([（(].*?[）)]).*?([（(].*?[）)]).*?', line)
                if rep_s:
                    for i in rep_s:
                        for j in i:
                            if j:
                                line = line.replace(j, '')
                rep_s = re.findall(r'.*?([(（].*[)）]).*', line)
                if rep_s:
                    for i in rep_s:
                        line = line.replace(i, '')
            # 第三步  去【】
            if '【' in line and '】' in line:
                rep_s = re.findall(r'.*?([【].*?[】]).*', line)
                if rep_s:
                    for i in rep_s:
                        line = line.replace(i, '')
            # 第四步  去《》
            if '《' in line and '》' in line:
                rep_s = re.findall(r'.*?([《].*?[》]).*', line)
                if rep_s:
                    for i in rep_s:
                        line = line.replace(i, '')
            if '《' in line and '》' in line:
                rep_s = re.findall(r'.*?([《].*?[》]).*', line)
                if rep_s:
                    for i in rep_s:
                        line = line.replace(i, '')
            res.add(line)

    print(len(res))
    fr.close()
    fw = open(f'../resume_project/data/job/job3.txt', 'w')
    for i in res:
        fw.write(str(i) + '\n')
    fw.close()


def test():
    fr = open(f'../resume_project/data/job/job3.txt')
    a = set()
    for line in fr:
        line = line.strip()
        if len(line) <= 2:
            print(line)
        if line:
            a.add(line.strip())
    s = '''工作职责：
        1.负责结合公司产品，进行语音合成相关产品研发；
        2.负责语音合成前端文本分析处理相关技术及模型训练；
        3.参与语音合成系统前端模块的设计、开发，包括文本预处理、分词、词性、韵律、语义理解等模块；
        4.负责跟踪国际最新算法发展方向和相关技术，将算法与解决方案进行产品转化。 
        
        任职要求：
        1.统招硕士及以上学历，计算机、电子信息和自动化等相关专业，1年以上相关工作经验；
        2.对数据结构和算法有较好的理解，熟练掌握python或C++，熟悉linux开发环境；
        3.了解语音模型或深度学习模型，具备较强的逻辑分析能力和数学基础；
        4.有机器学习基础，熟悉常见机器学习、深度学习算法，并对未知算法有技术好奇心；
        5.具有良好的团队沟通能力，优秀的逻辑思维能力，对解决挑战性问题充满热情，善于解决问题和分析问题；
        6.熟悉常用的深度学习框架（PyTorch/TensorFlow）者优先；
        7.有语音领域相关经历者优先，有ICASSP、INTERSPEECH或其他相关顶会论文优先。
        '''
    res = set()
    for i in a:
        if i in s:
            print(i)
            res.add(i)
    print(len(res))


if __name__ == '__main__':
    mul_pro_gen_library()
    # process_welfare()
    # process_company()
    # process_job()
    # process_industry()
    # test()
    get_company_industry()
