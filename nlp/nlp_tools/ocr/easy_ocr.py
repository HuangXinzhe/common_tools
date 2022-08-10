# # 导入easyocr
# import easyocr
# # 创建reader对象
# reader = easyocr.Reader(['ch_sim','en'])
# # 读取图像
# result = reader.readtext('2.pdf')
# # 结果
# print(result)

# import pytesseract
# from PIL import Image
# img = Image.open('2.pdf')
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# s = pytesseract.image_to_string(img, lang='chi_sim')  #不加lang参数的话，默认进行英文识别
# print(s)

from PIL import Image
import pytesseract
image = Image.open('101pdf.jpg')#打开图片
result = pytesseract.image_to_string(image,lang='chi_sim')#使用简体中文字库识别图片并返回结果
print(result)#打印识别的图片内容