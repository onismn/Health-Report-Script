from crewai import Task
from textwrap import dedent

class HealthDocumentTasks:
    def pdf_ingestion_task(self, agent, pdf_url):
        return Task(
            description=dedent(f"""
            **Task**: Medical Document Ingestion and Vector Storage
            **Description**: 
            1. Retrieve PDF document from the provided URL
            2. Extract full text content using OCR if necessary
            3. Preprocess and clean extracted text
            4. Store document content in vector database for semantic search
            5. Ensure document is fully parsed and searchable

            URL of PDF document: {pdf_url}
            """),
            agent=agent,
            expected_output="Full text content stored in vector database, ready for semantic querying"
        )

    def medical_insights_extraction_task(self, agent, context):
        return Task(
            description=dedent("""
            **Task**: Extract Key Medical Insights
            **Description**:
            1. Query vector database to extract relevant document sections
            2. Identify and extract 3-5 critical insights focusing on:
               - Diagnosed Conditions
               - Treatment Plans and Medications
               - Significant Lab or Diagnostic Findings
               - Next Steps in Care
            3. Translate medical terminology into layman's terms
            4. Ensure insights are patient-friendly and easily understandable
            5. Maintain medical accuracy while improving accessibility
            """),
            agent=agent,
            expected_output="JSON object containing 3-5 key medical insights in patient-friendly language",
            context=context
        )

    def patient_script_generation_task(self, agent, context):
        return Task(
            description=dedent("""
            **Task**: Generate Personalized Patient Communication Script
            **Description**:
            1. Use patient insights from previous task
            2. Create a concise script (120-150 words)
            3. Personalize script with patient's name
            4. Use second-person language
            5. Ensure logical flow of information
            6. Cover:
               - Diagnoses explanation
               - Treatment details
               - Next care steps
            7. Maintain conversational, supportive tone
            """),
            agent=agent,
            expected_output="JSON-formatted script addressing patient directly, summarizing medical insights",
            context=context,
            output_file='outputs/result.md'
        )
