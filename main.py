import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

from crewai import Crew, Process
from textwrap import dedent
import pymupdf

from agents import HealthDocumentAgents
from tasks import HealthDocumentTasks

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class HealthDocumentCrew:
    def __init__(self, pdf_url):
        self.pdf_url = pdf_url

    def run(self):
        # Initialize Agents
        agents = HealthDocumentAgents()
        tasks = HealthDocumentTasks()

        # Create Agents
        pdf_ingestion_agent = agents.pdf_ingestion_agent()
        medical_insights_agent = agents.medical_insights_agent()
        patient_script_generator = agents.patient_script_generator()

        # Create Tasks
        pdf_ingestion_task = tasks.pdf_ingestion_task(
            pdf_ingestion_agent, 
            self.pdf_url
        )
        
        medical_insights_task = tasks.medical_insights_extraction_task(
            medical_insights_agent, 
            [pdf_ingestion_task]
        )
        
        patient_script_task = tasks.patient_script_generation_task(
            patient_script_generator, 
            [medical_insights_task]
        )

        # Create Crew
        crew = Crew(
            agents=[
                pdf_ingestion_agent,
                medical_insights_agent,
                patient_script_generator
            ],
            tasks=[
                pdf_ingestion_task,
                medical_insights_task,
                patient_script_task
            ],
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )

        # Run the crew
        result = crew.kickoff()
        return result

def main():
    pdf_file_path = input(dedent("Upload your Patient Report in PDF (enter the file path): "))
    
    health_document_crew = HealthDocumentCrew(pdf_file_path)
    result = health_document_crew.run()
    
    print("\n\n##############################")
    print("## Medical Document Processing Result:")
    print("##############################\n")
    print(result)

if __name__ == "__main__":
    main()