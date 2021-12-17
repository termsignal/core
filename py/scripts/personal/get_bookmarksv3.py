# splitpdf.py start_raw_page end_raw_page file.pdf

import sys


from PyPDF2 import PdfFileReader, PdfFileWriter, generic


class bm():
    space = 0
    pg = []

    def __init__(self, path, pdf, lns) -> None:
        self.path = path
        self.pdf = pdf
        self.lns = lns
        self.run()
        self.chapters(bm.pg)

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
        no = []
        if type(item) == list:
            self.sublist(item)
        if type(item) == generic.Destination:
            # line = str(bm.space * " " + item['/Title'])
            page_no = pdf.getDestinationPageNumber(item)
            title = item['/Title']
            trail = "." * (55 - len(title))
            print(" " * bm.space, title, trail, page_no + 1)
            bm.pg.append([title, page_no + 1, bm.space // 2])

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
    

    def chapters(self, chapters, level=1):
        x = []
        out = []
        # for i in chapters:
        #     if i[2] == level:
        #         print(i, i[1] - 1)
        for i in range(len(chapters) - 1):
             if chapters[i][2] == level:
                u = chapters[i]
                x.append(u)
        print("----- Chapters ------")
        for r in range(0, len(x) - 1):
            # print(x[r][0], x[r][1], x[r + 1][1] - 1)
            string = [x[r][0], x[r][1], x[r + 1][1] - 1]
            out.append(string)
        num = self.pdf.getNumPages()
        x[-1][2] = num
        out.append(x[-1])
        for i in out:
            print(i)
        return out


if __name__ == '__main__':
    p = str(sys.argv[1])
    pdf = PdfFileReader(p)
    lbs = pdf.getOutlines(p)
    bm(p, pdf, lbs)
