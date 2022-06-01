import pdfbox

p = pdfbox.PDFBox()
p.extract_text('/path/to/my_file.pdf')  # writes text to /path/to/my_file.txt
p.pdf_to_images('/path/to/my_file.pdf')  # writes images to /path/to/my_file1.jpg, /path/to/my_file2.jpg, etc.
p.extract_images('/path/to/my_file.pdf')  # writes images to /path/to/my_file-1.png, /path/to/my_file-2.png, etc.
