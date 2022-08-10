import pdfplumber

with pdfplumber.open(r"D:\简历项目\所有简历数据\IT/903.pdf") as pdf:

########################################################################################################################
    """
    pdfplumber.PDF类
    
    pdfplumber.PDF类代表一个PDF文件,主要有以下两个属性:
    .metadata  元数据键/值对字典，摘自PDF的“信息”。通常包括“CreationDate”(创建日期)、“ModDate”(修改日期)、“Producer”(创建者)等。
    .pages  包含pdfplumber.Page(页实例)的列表。    
    """
########################################################################################################################
    """
    .metadata属性（PDF各类信息）
    元数据键/值对字典，摘自PDF的“信息”。通常包括“CreationDate”(创建日期)、“ModDate”(修改日期)、“Producer”(创建者)等。
    
    {'ModDate': "D:20210812112334+08'00'", 
    'CreationDate': "D:20210812112334+08'00'", 
    'Producer': 'iText 2.1.7 by 1T3XT; modified using iText® 5.4.2 ©2000-2012 1T3XT BVBA (AGPL-version)'}
    """
    # print(pdf.metadata)


    """
    .pages属性
    包含pdfplumber.Page(页实例)的列表。
    
    {'fontname': 'XSEYEZ+SimHei', 'adv': 9.0, 'upright': True, 'x0': 243.11, 'y0': 779.74, 
    'x1': 252.11, 'y1': 788.875, 'width': 9.0, 'height': 9.134999999999991, 
    'size': 9.134999999999991, 'object_type': 'char', 'page_number': 1, 'text': '简', 
    'top': 52.125, 'bottom': 61.25999999999999, 'doctop': 52.125}
    """
    # 第一页第一个字符
    # first_page = pdf.pages[0]
    # print(first_page.chars[0])

########################################################################################################################
    """
    pdfplumber.Page类
    
    pdfplumber.Page是pdfplumber核心. 大部分的操作都是围绕此类进行.主要包含以下属性:
    .page_number	页码, 1第一页, 2第二页, 以此类推.
    .width	页面宽.
    .height	页面高.
    .objects / .chars / .lines / .rects / .curves / .images	这些属性中的每一个都是一个列表，每个列表都为嵌入在页面上的每个此类对象
    包含一个字典。有关详细信息，请参见 "Objects".    
    
    方法：
    .crop(bounding_box, relative=False)
    """
########################################################################################################################
    text = ''
    for page in pdf.pages:

        # print(page.page_number)

        # print(page.width)

        # print(page.height)

        # print(page.objects)

        #
        # bounding_box = (1, 10, 300, 500)
        # print(page.crop(bounding_box, relative=False))

        # .extract_text(x_tolerance=3, y_tolerance=3, layout=False, x_density=7.25, y_density=13, **kwargs)
        print(page.extract_text())
        break