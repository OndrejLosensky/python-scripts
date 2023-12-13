import PyPDF2
import os
import time

# Very simple function to merge pdfs
def pdf_merge(pdfs_path, output_path):
    merge_tool = PyPDF2.PdfMerger()

    files = [f for f in os.listdir(pdfs_path) if os.path.isfile(os.path.join(pdfs_path, f))]

    pdf_files = [os.path.join(pdfs_path, f) for f in files if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("No PDF files were found! Please create some and try it again")
        return

    for pdf_file in pdf_files:
        merge_tool.append(pdf_file)

    with open(output_path, 'wb') as output_file:
        merge_tool.write(output_path)

def main():
    print("Initializing the process...")
    start_time = time.time()
    input_path = "src/PDFS_to_Merge"

    output_path = "merged_file.pdf"
    print("PDF's loaded!")

    pdf_merge(input_path, output_path)
    print(f"Process successfull. PDF's were merged to: {output_path}")
    
    time_it_took = time.time() - start_time
    formatedTime = "{:.2f}".format(time_it_took)
    print("It took ", formatedTime, "seconds")

if __name__ == "__main__":
    main()