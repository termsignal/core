import dropbox
dbx = dropbox.Dropbox("27ktrl9e7sjavmt")

with open("Prime_Numbers.txt", "wb") as f:
    metadata, res = dbx.files_download(path="/Homework/math/Prime_Numbers.txt")
    f.write(res.content)
