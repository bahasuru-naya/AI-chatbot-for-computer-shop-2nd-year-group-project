# Loan Management System

A Flask-based web application that uses LangChain and Google's Gemini model to provide intelligent loan information retrieval and management. The system connects to a MongoDB database and uses RAG (Retrieval Augmented Generation) to answer queries about loan information.

## Features

- Interactive web interface for querying loan information
- Real-time responses using Google's Gemini AI model
- MongoDB integration for loan data storage
- Vector-based search using FAISS
- Responsive design with error handling
- Support for various loan-related queries

## Prerequisites

- Python 3.8 or higher
- MongoDB database with loan information
- Google API key for Gemini model
- Git (optional, for version control)

## Project Structure

```
loan_management/
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── .env                  # Environment variables
└── templates/
    └── index.html        # Frontend template
```

## Installation

1. Clone the repository (if using Git):
```bash
git clone <repository-url>
cd loan_management
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_google_api_key_here
```

### Expected MongoDB Schema

Your MongoDB collection should have the following fields:
- _id
- customer_id
- first_name
- last_name
- date_of_birth
- address
- phone
- email
- national_id
- loan_id
- loan_type
- principal_amount
- interest_rate
- loan_term_months
- start_date
- end_date
- loan_status
- collaterals
- repayments
- payment_schedule
- loan_application
- assigned_employee
- branch

## Running the Application

1. Make sure your virtual environment is activated
2. Start the Flask server:
```bash
python app.py
```
3. Open a web browser and navigate to:
```
http://localhost:5000
```

## Usage

### Example Queries

You can ask various questions about loan information, such as:
- "Loan information on CUST001"
- "What is the repayment history for Loan ID LOAN123?"
- "Who is the assigned employee for Customer ID CUST456?"
- "Provide details about the collateral for Loan ID LOAN789"
- "What is the loan status for Customer ID CUST001?"

### Response Format

The system provides structured responses including:
1. Customer Information
2. Loan Information
3. Collateral Details
4. Repayment History
5. Payment Schedule
6. Employee Information
7. Branch Information

## Troubleshooting

Common issues and solutions:

1. **MongoDB Connection Error**
   - Verify your MongoDB connection string
   - Check if the MongoDB server is running
   - Ensure network connectivity

2. **Google API Key Issues**
   - Verify the API key in your `.env` file
   - Check if the API key has the necessary permissions
   - Ensure the key is properly activated in Google Cloud Console

3. **Application Not Starting**
   - Check if all dependencies are installed
   - Verify Python version compatibility
   - Look for error messages in the console
