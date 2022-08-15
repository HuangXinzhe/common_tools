from cnocr import CnOcr
from utils import file_name
import time

# 简单用法
# img_fp = r'D:\common_tools\common_tools\nlp\nlp_tools\imagepdf_to_image\image_1\101_0.jpg'
#
# ocr = CnOcr()  # 所有参数都使用默认值
#
# out = ocr.ocr(img_fp)

start_time = time.time()
all_jpg = file_name('../imagepdf_to_image/image_1/')
txt_content = ''
for single_jpg in all_jpg:
    img_fp = f'../imagepdf_to_image/image_1/{single_jpg}'
    ocr = CnOcr()  # 所有参数都使用默认值
    # ocr = CnOcr(rec_model_name='ch_PP-OCRv3')  # 所有参数都使用默认值
    out = ocr.ocr(img_fp)
    print(out)
    for line_number in range(len(out)):
        if line_number == 0:
            txt_content += out[line_number]['text']
        else:
            if abs(out[line_number - 1]['position'][0][1] - out[line_number]['position'][0][1]) <= 15:
                txt_content += ' ' + out[line_number]['text']
            else:
                txt_content += '\n' + out[line_number]['text']
    txt_content += '\n'
print(txt_content)
end_time = time.time()
print(end_time-start_time)