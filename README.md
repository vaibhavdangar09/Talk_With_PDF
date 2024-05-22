
---

# Setting Up Python 3.11 Environment and OpenAI API for App

This guide will walk you through the steps to set up a Python 3.11 environment, create a virtual environment, activate it, set up your OpenAI API key, and finally run your `app.py` file.

## Steps:

1. **Install Python 3.11:**

    ```
    python install 3.11
    ```

2. **Create a Virtual Environment:**

    To create a virtual environment named `venv`, run the following command:

    ```
    python -m venv venv
    ```

3. **Activate Your Virtual Environment:**

    To activate the virtual environment, use the following command:

    ```
    source venv/bin/activate
    ```

4. **Set Up Your OpenAI API Key:**

    After activating your virtual environment, add your OpenAI API key to the `bashrc` file:

    ```
    export OPENAI_API_KEY="enter_your_key"
    ```

    Replace `"enter_your_key"` with your actual OpenAI API key.

5. **Run Your App:**

    Once you've completed all the above steps, you can start running your `app.py` file. Use the following command:

    ```
    streamlit run app.py
    ```

    This will launch your Streamlit application.


# Project Description: Talk_with_PDF
## Overview:

** Talk_with_PDF is an innovative project leveraging advanced Large Language Models (LLMs) and Generative AI (GenAI) technologies from OpenAI to provide automated, intelligent responses to questions based on the content of a PDF document. This system integrates PDF document analysis with question-answering capabilities, making it a powerful tool for educational purposes, business analysis, and research assistance.**

Key Features:

1. PDF Upload and Analysis:

    Users can upload a PDF document to the system.
    The content of the PDF is processed and analyzed using OpenAI's language model and embeddings.
    CSV-based Question Handling:

2. Users upload
    a CSV file containing a set of questions related to the uploaded PDF.
    
    Each question in the CSV file is sequentially processed by the system.

3. Automated Question-Answering:
   
    The system utilizes OpenAI's language model to generate accurate and contextually relevant responses to each question based on the content of the PDF.
    The responses are generated using OpenAI embeddings to ensure high relevance and precision.

4. Response Storage:

    The generated responses are stored in a new CSV file, aligning with the original questions for easy reference and further analysis.

---
