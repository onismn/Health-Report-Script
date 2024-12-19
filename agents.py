from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.pdf_tools import PDFTools


class HealthDocumentAgents:
    def __init__(self):
        self.OpenAIGPT = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

    def pdf_ingestion_agent(self):
        return Agent(
            role="PDF Ingestion Specialist",
            backstory="Expert in extracting and storing medical document content with precision and confidentiality",
            goal="Ingest medical PDF documents, extract content using OCR if needed, and store in vector database for efficient semantic search",
            max_iter=5,
            tools=[PDFTools.extract_text_from_pdf],
            verbose=True,
            allow_delegation=False,
            llm=self.OpenAIGPT,
        )
        
    def medical_insights_agent(self):
        return Agent(
            role="Medical Insights Extractor",
            backstory="Specialized medical professional skilled in analyzing complex medical documents and extracting patient-relevant insights",
            goal="Extract and synthesize 3-5 key insights from medical documents, focusing on diagnoses, treatments, lab findings, and next steps",
            max_iter=5,
            verbose=True,
            allow_delegation=False,
            llm=self.OpenAIGPT,
        )

    def patient_script_generator(self):
        return Agent(
            role="Patient Communication Specialist",
            backstory="Expert in translating complex medical information into clear, compassionate, patient-friendly language",
            goal="Generate personalized, concise medical report scripts (120-150 words) that explain diagnoses and next steps",
            max_iter=5,
            verbose=True,
            allow_delegation=False,
            llm=self.OpenAIGPT,
        )
