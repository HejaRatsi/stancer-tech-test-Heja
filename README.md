# Stancer DSP2 - Technical Test

This project is a Python client implementation to interact with a PSD2-compliant API.

## Features

- OAuth2 authentication
- Fetch identity
- List user accounts
- Retrieve account balances
- List related transactions

## Installation

Make sure you're using **Python 3.11** or higher.

1. Clone the repository:
   ```bash
   git clone https://github.com/HejaRatsi/stancer-tech-test-Heja.git
   cd stancer-tech-test-Heja
   ```
   
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate     # on Unix/macOS
   venv\Scripts\activate        # on Windows
   ```
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables
   Create a .env file in the root directory by copying the example:
   ```bash
   cp .env.example .env
   ```
   Then fill in the credentials:
   ```bash
   API_BASE_URL=http://localhost:8000
   ```
   Do not commit your .env file, it must stay private. Use .env.example to share the structure only.
   

## Run the application 
   ```bash
   python main.py
   ```
