"""Split large PDFs into smaller chunks for OCR processing."""
import os
from PyPDF2 import PdfReader, PdfWriter

BASE = r"D:\作业&小组展示\大物PPT整理"
PDF_DIR = os.path.join(BASE, "PDF")
TEMP_DIR = os.path.join(BASE, "temp")

# ch9 original PDFs
files = [
    "大学物理ch9 静电场--1场强、高斯定理.pdf",
    "大学物理ch9 静电场--2电势.pdf",
    "大学物理ch9 静电场--3导体、电容.pdf",
    "大学物理ch9 静电场--4电介质.pdf",
]

CHUNK_SIZE = 8  # pages per chunk

os.makedirs(TEMP_DIR, exist_ok=True)

for fname in files:
    path = os.path.join(PDF_DIR, fname)
    if not os.path.exists(path):
        print(f"NOT FOUND: {path}")
        continue
    reader = PdfReader(path)
    total = len(reader.pages)
    prefix = os.path.splitext(fname)[0].replace("大学物理", "").replace(" ", "_")
    num_chunks = (total + CHUNK_SIZE - 1) // CHUNK_SIZE
    for i in range(num_chunks):
        start = i * CHUNK_SIZE
        end = min(start + CHUNK_SIZE, total)
        writer = PdfWriter()
        for p in range(start, end):
            writer.add_page(reader.pages[p])
        out_name = f"{prefix}_p{start+1}-{end}.pdf"
        out_path = os.path.join(TEMP_DIR, out_name)
        with open(out_path, "wb") as f:
            writer.write(f)
        print(f"  -> {out_name} ({end-start} pages)")
    print(f"[{fname}] {total} pages -> {num_chunks} chunks")

print("\nDone. All chunks in temp/")
