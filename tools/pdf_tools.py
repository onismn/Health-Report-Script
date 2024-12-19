import fitz
import openai
from langchain.tools import tool

class PDFTools():

    @tool("Extract PDF data")
    def extract_text_from_pdf(pdf_file_path):
        """
        A tool to extract text from PDF files and analyze it using GPT-4
        """
        doc = fitz.open(pdf_file_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        return text