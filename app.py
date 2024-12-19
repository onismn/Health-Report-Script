from flask import Flask, request, jsonify, render_template
from main import HealthDocumentCrew
import logging
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/process-medical-document', methods=['POST'])
def process_medical_document():
    try:
        # Validate request
        data = request.get_json()
        pdf_url = data.get('pdf_url')
        
        if not pdf_url:
            return jsonify({
                "error": "PDF URL is required",
                "status": "failed"
            }), 400
        
        # Initialize and run Crew
        health_document_crew = HealthDocumentCrew(pdf_url)
        result = health_document_crew.run()
        
        # Clean up the result string
        result_str = str(result)
        # Remove JSON formatting and extract just the script content
        if "```json" in result_str:
            import json
            # Extract the JSON string between the backticks
            json_str = result_str.split("```json\n")[1].split("\n```")[0]
            # Parse the JSON and get just the script content
            parsed_result = json.loads(json_str)
            cleaned_result = parsed_result.get("script", "No script generated")
        else:
            cleaned_result = result_str
        
        # Prepare response
        response = {
            "status": "success",
            "result": cleaned_result,
            "metadata": {
                "pdf_url": pdf_url,
                "processing_timestamp": datetime.now().isoformat()
            }
        }
        
        logging.info(f"Successfully processed document: {pdf_url}")
        return jsonify(response), 200
    
    except Exception as e:
        logging.error(f"Error processing document: {str(e)}")
        return jsonify({
            "error": str(e),
            "status": "failed"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "Medical Document Processing API"
    }), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)