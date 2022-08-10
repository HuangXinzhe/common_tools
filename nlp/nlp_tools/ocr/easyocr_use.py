import easyocr
reader = easyocr.Reader(['ch_sim', 'en'], gpu=False, model_storage_directory='./model')
# result_detect = reader.detect('124pdf.jpg')
result_readtext = reader.readtext('../imagepdf_to_image/image_2/124pdf_0.jpg')
# print(result_detect)
print(result_readtext)

# txt_content = ''
# for line_number in range(len(result_readtext)):
#     if line_number == 0:
#         txt_content += result_readtext[line_number][1][0]
#     else:
#         if abs(result_readtext[line_number - 1][0][0][1] - result_readtext[line_number][0][0][1]) <= 10:
#             txt_content += ' ' + result_readtext[line_number][1][0]
#         else:
#             txt_content += '\n' + result_readtext[line_number][1][0]
# txt_content += '\n'
# print(txt_content)