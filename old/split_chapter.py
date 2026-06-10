import os
from PyPDF2 import PdfReader, PdfWriter

base = r"D:\作业&小组展示\大物PPT整理"
example_dir = os.path.join(base, "例题+答案")
temp_dir = os.path.join(base, "temp")

def split_pdf(input_path, output_prefix):
    """Split a PDF into single pages."""
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    for i in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        output_file = os.path.join(temp_dir, f"{output_prefix}_page{i+1}.pdf")
        with open(output_file, "wb") as f:
            writer.write(f)
        print(f"  Created: {output_file}")
    return total_pages

# Process chapter 1
chapter = 1
example_file = os.path.join(example_dir, f"ch{chapter}-例题.pdf")
answer_file = os.path.join(example_dir, f"ch{chapter}-例题答案.pdf")

if os.path.exists(example_file):
    print(f"Splitting chapter {chapter} example PDF:")
    pages = split_pdf(example_file, f"ch{chapter}_example")
    print(f"Total pages: {pages}")
else:
    print(f"Example file not found: {example_file}")

if os.path.exists(answer_file):
    print(f"\nSplitting chapter {chapter} answer PDF:")
    pages = split_pdf(answer_file, f"ch{chapter}_answer")
    print(f"Total pages: {pages}")
else:
    print(f"Answer file not found: {answer_file}")