# splitpdf.py start_raw_page end_raw_page file.pdf

from os import name
import sys
import re

from PyPDF2 import PdfFileReader, PdfFileWriter

class spitz():
        
    def split(self, path, name_of_split, start, end):
        pdf = PdfFileReader(path)
        name = re.sub('[^A-Za-z0-9]+ ', ' ', str(name_of_split))

        # for i in pdf.getOutlines(path):
        #     if type(i) == list:
        #         print(i[0], "\n")
        #     print(i.keys, "\n")
        pdf_writer = PdfFileWriter()
        output = f'{name}.pdf'
        for page in range(int(start) - 1, int(end) - 1):
            pdf_writer.addPage(pdf.getPage(page))

        with open(output, "wb") as out:
                pdf_writer.write(out)
        return output


    # split(str(sys.argv[3]), 'Chapter-', sys.argv[1], sys.argv[2])
