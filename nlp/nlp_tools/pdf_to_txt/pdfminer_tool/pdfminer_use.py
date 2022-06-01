from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import copy
from tika import parser
import logging


def set_log():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.WARNING)
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


class read_file:
    def __init__(self):
        'self.read_way_flag:0 is tika,1 is pdfminer'
        self.read_way_flag = 0
        self.is_left_right_file = 0
        self.logger = set_log()

    def read_pdf(self, file_path):
        fp = open(file_path, 'rb')
        parser = PDFParser(fp)
        pdfDocument = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        self.pages_x = []
        self.pages_y = []
        self.pages_contents = []
        for page in PDFPage.create_pages(pdfDocument):
            interpreter.process_page(page)
            layout = device.get_result()
            page_x = []
            page_y = []
            page_contents = []
            for textbox in layout:
                if isinstance(textbox, LTTextBox) or isinstance(textbox, LTTextLine):
                    for char in textbox:
                        if char.get_text().strip() != '':
                            _a = []
                            _a.append(char.bbox[0])
                            _a.append(char.bbox[2])
                            page_x.append(_a)
                            page_y.append((char.bbox[1], char.bbox[3]))
                            page_contents.append((char.get_text().strip() + ''))
            self.pages_x.append(page_x)
            self.pages_y.append(page_y)
            self.pages_contents.append(page_contents)
        return self.pages_x, self.pages_y, self.pages_contents


if __name__ == "__main__":
    read = read_file()
    # print(read.read_pdf('/Users/greedy/Documents/所有简历数据/IT/29.pdf'))
    print(read.read_pdf(r'D:\简历项目\所有简历数据\IT/29.pdf'))
