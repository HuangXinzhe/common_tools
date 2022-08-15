import fitz
import re

file = r'D:\简历项目\所有简历数据\IT/333.pdf'
pdfDoc = fitz.open(file)
for pg in range(pdfDoc.pageCount):
    page = pdfDoc[pg]
    rotate = int(0)
    zoom_x = 2
    zoom_y = 2
    mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
    pix = page.get_pixmap(matrix=mat, alpha=False)

    file_name = re.search('(.*)/(.*).pdf', file).group(2)
    pix.writePNG('./image_5/' + f'{file_name}_{pg}.jpg')  # 将图片写入指定的文件夹内