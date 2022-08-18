import random
from utils import file_name

file_name_list = file_name(r'D:\简历项目\所有简历数据\IT')
pdf_list = []
image_pdf = ['101.pdf', '1015.pdf', '1043.pdf', '1061.pdf', '1069.pdf', '1140.pdf', '1184.pdf', '1207.pdf', '121.pdf', '124.pdf', '1244.pdf', '1258.pdf', '1264.pdf', '1280.pdf', '1284.pdf', '1291.pdf', '1297.pdf', '13.pdf', '1343.pdf', '1346.pdf', '1355.pdf', '1360.pdf', '1361.pdf', '1381.pdf', '1382.pdf', '1383.pdf', '1388.pdf', '1407.pdf', '1434.pdf', '1458.pdf', '1471.pdf', '1513.pdf', '1560.pdf', '1567.pdf', '1597.pdf', '1621.pdf', '1664.pdf', '1687.pdf', '169.pdf', '1691.pdf', '1722.pdf', '1726.pdf', '1765.pdf', '177.pdf', '179.pdf', '1798.pdf', '1799.pdf', '1827.pdf', '1843.pdf', '1845.pdf', '185.pdf', '1856.pdf', '1865.pdf', '19.pdf', '1907.pdf', '1917.pdf', '1921.pdf', '1925.pdf', '1944.pdf', '1953.pdf', '1963.pdf', '1964.pdf', '1968.pdf', '1975.pdf', '1985.pdf', '2.pdf', '273.pdf', '333.pdf', '358.pdf', '371.pdf', '392.pdf', '4.pdf', '401.pdf', '405.pdf', '406.pdf', '467.pdf', '478.pdf', '48.pdf', '483.pdf', '498.pdf', '500.pdf', '535.pdf', '553.pdf', '568.pdf', '572.pdf', '594.pdf', '598.pdf', '604.pdf', '608.pdf', '613.pdf', '654.pdf', '664.pdf', '702.pdf', '71.pdf', '713.pdf', '726.pdf', '737.pdf', '757.pdf', '787.pdf', '792.pdf', '870.pdf', '888.pdf', '902.pdf', '910.pdf', '93.pdf', '930.pdf', '939.pdf', '952.pdf', '954.pdf', '971.pdf', '991.pdf']
for file in file_name_list:
    if 'pdf' in file and file not in image_pdf:
        pdf_list.append(file)
sample_num = 1
print(random.sample(pdf_list, sample_num))