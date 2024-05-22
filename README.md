
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

---