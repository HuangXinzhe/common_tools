import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from paddleocr import PaddleOCR, draw_ocr
from utils import file_name
from PIL import Image
import time

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
start_time = time.time()
all_jpg = file_name('../imagepdf_to_image/image_1/')
txt_content = ''
for single_jpg in all_jpg:
    img_path = f'../imagepdf_to_image/image_1/{single_jpg}'
    result = ocr.ocr(img_path, cls=True)

    # print(result)
    # print(result[0][0])
    # print(result[0][0][0])
    # for line in result:
    #     print(line)

    for line_number in range(len(result)):
        if line_number == 0:
            txt_content += result[line_number][1][0]
        else:
            if abs(result[line_number - 1][0][0][1] - result[line_number][0][0][1]) <= 10:
                txt_content += ' ' + result[line_number][1][0]
            else:
                txt_content += '\n' + result[line_number][1][0]
    txt_content += '\n'

    # image_1 = Image.open(img_path).convert('RGB')
    # boxes = [line[0] for line in result]
    # txts = [line[1][0] for line in result]
    # scores = [line[1][1] for line in result]
    # im_show = draw_ocr(image_1, boxes, txts, scores, font_path='./fonts/simfang.ttf')
    # im_show = Image.fromarray(im_show)
    # im_show.save(f'./result/result_{single_jpg}')


print(txt_content)
end_time = time.time()
print(end_time-start_time)

# 显示结果
# from PIL import Image

# image_1 = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image_1, boxes, txts, scores, font_path='./fonts/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('101pdf.jpg')
