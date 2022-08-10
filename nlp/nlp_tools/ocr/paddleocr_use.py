import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from paddleocr import PaddleOCR, draw_ocr
from utils import file_name
from PIL import Image

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
all_jpg = file_name(r'D:\PycharmProjects\resume_project\text_convert\ocr\resume_pdf_image/')
txt_content = ''
for single_jpg in all_jpg:
    img_path = f'D:/PycharmProjects/resume_project/text_convert/ocr/resume_pdf_image/{single_jpg}'
    result = ocr.ocr(img_path, cls=True)

    # print(result[0])
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

    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(f'124pdf_{single_jpg}')


print(txt_content)

# 显示结果
# from PIL import Image

# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('101pdf.jpg')
