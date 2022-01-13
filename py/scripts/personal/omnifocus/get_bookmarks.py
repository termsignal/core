# splitpdf.py start_raw_page end_raw_page file.pdf

import sys


from PyPDF2 import PdfFileReader, PdfFileWriter, generic


class bm():
    space = 0

    def __init__(self, path, pdf, lns) -> None:
        self.path = path
        self.pdf = pdf
        self.lns = lns
        self.run()

    # @classmethod
    def run(self):
        print()
        for l in self.lns:
            if type(l) == list:
                self.sublist(l)
            if type(l) == generic.Destination:
                self.bookmark(l)

    @classmethod
    def bookmark(self, item):
        if type(item) == list:
            self.sublist(item)
        if type(item) == generic.Destination:
            print(" " * bm.space, item['/Title'])

    @classmethod
    def sublist(self, item):
        if type(item) == generic.Destination:
            self.bookmark(item)
        if type(item) == list:
            bm.space += 2
            for x in item:
                self.bookmark(x)
                if x == item[-1]:
                    bm.space -= 2


if __name__ == '__main__':
    p = str(sys.argv[3])
    pdf = PdfFileReader(p)
    lbs = pdf.getOutlines(p)
    bm(p, pdf, lbs)
