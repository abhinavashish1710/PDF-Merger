import os
from pypdf import PdfWriter

input_folder = "sample_pdfs"
output_folder = "output"
output_file = os.path.join(output_folder, "merged.pdf")

os.makedirs(output_folder, exist_ok=True)

pdf_files = sorted(
    f for f in os.listdir(input_folder)
    if f.lower().endswith(".pdf")
)

if not pdf_files:
    print("No PDF files found in sample_pdfs.")
    exit()

writer = PdfWriter()

for pdf in pdf_files:
    file_path = os.path.join(input_folder, pdf)
    writer.append(file_path)
    print(f"Added: {pdf}")

with open(output_file, "wb") as f:
    writer.write(f)

writer.close()

print(f"\nSuccessfully merged {len(pdf_files)} PDF(s).")
print(f"Saved to: {output_file}")