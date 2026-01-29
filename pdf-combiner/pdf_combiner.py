from pypdf import PdfReader, PdfWriter
import argparse

def combine_pdfs(pdf1_path, pdf2_path, output_path="combined.pdf"):
    """
    Combines two PDFs into a single PDF.
    
    Args:
        pdf1_path (str): Path to the first PDF
        pdf2_path (str): Path to the second PDF
        output_path (str): Path for the output combined PDF
    """
    writer = PdfWriter()
    
    # Add all pages from first PDF
    reader1 = PdfReader(pdf1_path)
    for page in reader1.pages:
        writer.add_page(page)
    
    # Add all pages from second PDF
    reader2 = PdfReader(pdf2_path)
    for page in reader2.pages:
        writer.add_page(page)
    
    # Write the combined PDF
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    
    print(f"Combined PDF saved to: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine two PDFs into one")
    parser.add_argument("pdf1", help="Path to the first PDF")
    parser.add_argument("pdf2", help="Path to the second PDF")
    parser.add_argument("-o", "--output", default="combined.pdf", help="Output path (default: combined.pdf)")
    
    args = parser.parse_args()
    combine_pdfs(args.pdf1, args.pdf2, args.output)