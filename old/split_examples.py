"""Split example PDFs into single pages for OCR."""
import os
from PyPDF2 import PdfReader, PdfWriter

BASE = r"D:\作业&小组展示\大物PPT整理"
EX_DIR = os.path.join(BASE, "例题+答案")
TEMP_DIR = os.path.join(BASE, "temp")

files = ["ch9-例题.pdf", "ch9-例题答案.pdf"]

for fname in files:
    path = os.path.join(EX_DIR, fname)
    if not os.path.exists(path):
        print(f"NOT FOUND: {path}")
        continue
    reader = PdfReader(path)
    total = len(reader.pages)
    prefix = os.path.splitext(fname)[0]
    for i in range(total):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        out_name = f"{prefix}_p{i+1}.pdf"
        out_path = os.path.join(TEMP_DIR, out_name)
        with open(out_path, "wb") as f:
            writer.write(f)
        print(f"  {out_name}")
    print(f"[{fname}] {total} pages split")

print("Done.")
