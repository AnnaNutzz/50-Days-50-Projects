"""
Generates a merged pdf file of 2 files given as input from user in Downloads folder.

"""

import PyPDF2
import os

def merge_pdfs(file1_path, file2_path, output_file):
    """Merges two PDF files into a single output file.

    file1_path : Path to the first PDF file.
    file2_path : Path to the second PDF file.
    output_file : Path to the output merged PDF file.
    """

    try:
        pdf_writer = PyPDF2.PdfWriter()

        with open(file1_path, 'rb') as pdf_file1:
            pdf_reader1 = PyPDF2.PdfReader(pdf_file1)
            for page_num in range(len(pdf_reader1.pages)):
                page = pdf_reader1.pages[page_num]
                pdf_writer.add_page(page)

        with open(file2_path, 'rb') as pdf_file2:
            pdf_reader2 = PyPDF2.PdfReader(pdf_file2)
            for page_num in range(len(pdf_reader2.pages)):
                page = pdf_reader2.pages[page_num]
                pdf_writer.add_page(page)

        with open(output_file, 'wb') as output_file:
            pdf_writer.write(output_file)

        print("PDFs merged successfully!")

    except Exception as e:
        print(f"Error merging PDFs: {e}")

def main():
    download_folder = "C:/Users/askah/Downloads"
    pdf_files = [f for f in os.listdir(download_folder) if f.endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the downloads folder.")
        return

    print("Available PDF files:")
    for i, file in enumerate(pdf_files):
        print(f"{i+1}. {file}")

    while True:
        try:
            file1_index = int(input("Enter the index of the first PDF file: ")) - 1
            file2_index = int(input("Enter the index of the second PDF file: ")) - 1

            if not (0 <= file1_index < len(pdf_files) and 0 <= file2_index < len(pdf_files)):
                raise ValueError("Invalid file indices")

            file1_path = os.path.join(download_folder, pdf_files[file1_index])
            file2_path = os.path.join(download_folder, pdf_files[file2_index])
            output_file = os.path.join(download_folder, "merged.pdf")

            merge_pdfs(file1_path, file2_path, output_file)
            break

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
