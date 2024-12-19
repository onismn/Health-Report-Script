## How to Run

Follow these steps to run the Agent:

1. **Clone the repository**:
   ```
   git clone https://github.com/onismn/Health-Report-Script
   cd Health-Report-Script
   ```

2. **Set up the environment**:
   Ensure you have Python 3.11.0 to 3.11.2 installed. Then, install Poetry if you haven't already:
   ```
   pip install poetry
   ```

3. **Install dependencies**:
   ```
   poetry install
   ```

4. **Set up your API keys**:
   Create a `.env` file in the project root and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

5. **Run the application**:
   ```
   poetry run python main.py
   ```

6. **Follow the prompts**:
   When prompted, enter the file path to your blood test report PDF.

7. **Review the results**:
   The program will output a script based on the blood test results.
