# import os
# import pandas as pd
# import streamlit as st
# from PyPDF2 import PdfReader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI
# from langchain.callbacks import get_openai_callback


# def main():
#     st.set_page_config(page_title="Ask your PDF")
#     st.header("Ask your PDF 💬")

#     # upload file
#     pdf = st.file_uploader("Upload your PDF", type="pdf")

#     # extract the text
#     if pdf is not None:
#         pdf_reader = PdfReader(pdf)
#         text = ""
#         for page in pdf_reader.pages:
#             text += page.extract_text()

#         # split into chunks
#         text_splitter = CharacterTextSplitter(
#             separator="\n",
#             chunk_size=1000,
#             chunk_overlap=200,
#             length_function=len
#         )
#         chunks = text_splitter.split_text(text)

#         # create or load existing CSV file for the PDF
#         csv_filename = os.path.splitext(pdf.name)[0] + ".csv"
#         if os.path.exists(csv_filename):
#             df = pd.read_csv(csv_filename)
#         else:
#             df = pd.DataFrame(columns=["Question", "Response"])

#         # create embeddings
#         embeddings = OpenAIEmbeddings()
#         knowledge_base = FAISS.from_texts(chunks, embeddings)
#         user_question = st.text_input("Ask a question about your PDF:")
#         if user_question:
#             docs = knowledge_base.similarity_search(user_question)
#             llm = OpenAI()
#             chain = load_qa_chain(llm, chain_type="stuff")
#             with get_openai_callback() as cb:
#                 response = chain.run(input_documents=docs, question=user_question)
#                 print(cb)

#             # check if the question is already present in the CSV
#             if user_question not in df["Question"].values:
#                 new_data = {"Question": user_question, "Response": response}
#                 df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
#                 df.to_csv(csv_filename, index=False)  # save the updated CSV file

#             st.write(response)


# if __name__ == '__main__':
#     main()







import os
import pandas as pd
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import time

def main():
    st.set_page_config(page_title="Ask your PDF", layout="centered")
    st.title("Ask your PDF 💬")
    # Sidebar for upload functionality
    st.sidebar.header("Upload")
    pdf = st.sidebar.file_uploader("Upload PDF", type="pdf")
    questions_csv = st.sidebar.file_uploader("Upload CSV with Questions", type="csv")
    csv_submit = st.sidebar.button("Submit CSV", key="csv_submit")

    # Main content area
    response_container = st.container()

    # Extract text from PDF and process questions
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        text_splitter = CharacterTextSplitter(
            separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Create or load existing CSV file for the PDF
        csv_filename = os.path.splitext(pdf.name)[0] + ".csv"
        if os.path.exists(csv_filename):
            df = pd.read_csv(csv_filename)
        else:
            df = pd.DataFrame(columns=["Question", "Response"])

        # Create embeddings and knowledge base
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)
        st.sidebar.button("PDF Submitted", key="pdf_submitted", disabled=True)

        # Process questions from CSV and generate responses
        if questions_csv is not None and csv_submit:
            questions_df = pd.read_csv(questions_csv)
            for index, row in questions_df.iterrows():
                user_question = row["Question"]
                docs = knowledge_base.similarity_search(user_question)
                llm = OpenAI()
                chain = load_qa_chain(llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=user_question)

                with response_container:
                    st.write(f"### Question: {user_question}")
                    
                    
                    response_lines = response.split("\n")
                    for line in response_lines:
                        st.write(line)
                        time.sleep(0.5)  
                        

                # Append response to responses dataframe
                if user_question not in df["Question"].values:
                    new_data = {"Question": user_question, "Response": response}
                    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            
                time.sleep(1)

            # Save responses to CSV file
            st.write("Saving responses to CSV...")
            df.to_csv(csv_filename, index=False)
            st.write("Responses saved successfully.")
            st.sidebar.button("CSV Submitted", key="csv_submitted", disabled=True)

if __name__ == '__main__':
    main()

