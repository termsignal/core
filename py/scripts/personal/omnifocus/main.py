import sys

from get_bookmarksv4 import bm
from create_project import addtoomni
from splitPDF import spitz
from send_to_gcp import upload
import webbrowser as wb

from PyPDF2 import PdfFileReader, PdfFileWriter, generic


p = str(sys.argv[1])
pdf = PdfFileReader(p)
lbs = pdf.getOutlines(p)
x = bm(p, pdf, lbs)
a = addtoomni()
u = upload()
urls = []
p_emoji = a.emojiz()
for y in x.o:
    y[0] = str(y[0]).replace('/', '')

    # s.split(p, y[0], y[1], y[2])
    s = spitz()
    w = s.split(p, y[0], y[1], y[2])
    y[0] = a.emojiz() + "  " + str(y[0])
    q = u.upload_blob(
        bucket_name='books-study',
        source_file_name=w,
        destination_blob_name=sys.argv[2] + '/' + w,
    )
    # print(y[0], '------------>', q)
    urls.append(a.request(p_emoji, sys.argv[2], y[0], q))

for i in urls:
    wb.open_new_tab(i)
    print(i + "\n")