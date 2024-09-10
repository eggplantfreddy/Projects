import PyPDF2

def extract_text_from_pdf(pdf_path, start_page=0, end_page=None):
    """
    Extracts text from a given PDF between the specified pages.
    If no end_page is specified, it will extract until the last page.
    
    Parameters:
    - pdf_path: Path to the PDF file.
    - start_page: The page number (0-indexed) to start extracting from.
    - end_page: The page number (0-indexed) to stop extracting at. If None, extract till the last page.
    
    Returns:
    - extracted_text: The text extracted from the PDF.
    """
    extracted_text = ""

    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        number_of_pages = len(reader.pages)

        # If end_page is not specified, read till the last page
        if end_page is None or end_page > number_of_pages:
            end_page = number_of_pages

        # Extract text from the specified page range
        for page_num in range(start_page, end_page):
            page = reader.pages[page_num]
            extracted_text += page.extract_text()

    return extracted_text

# Example Usage:
pdf_file_path = "example.pdf"
start_page = 3  # Page to start extraction (0-indexed)
end_page = 5    # Page to end extraction (0-indexed)

# Extract text from pages 3 to 5
text = extract_text_from_pdf(pdf_file_path, start_page, end_page)
print(text)
