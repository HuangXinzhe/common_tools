import easyocr
reader = easyocr.Reader(['ch_sim', 'en'], gpu=False, model_storage_directory='./model')
result = reader.detect('ceshi.png')
print(result)