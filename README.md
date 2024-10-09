# Chat_with_any_pdf
Upload File and chat with pdf

Welcome to the Chat with PDF Project by Pratik Kumar

This project leverages LLM models to extract data from PDF files. A script has been developed to enable seamless integration with Jupyter notebooks for data extraction. The process involves two key steps:

Providing the model with the PDF for information retrieval in simpler language.
Querying the model with specific questions and the PDF file name for accurate results.
Getting Started

1. Save the PDF file in the 'research_papers' folder.
2. Use the command "from read_pdf import import EmbedPDF, QueryPDF".
3. Generate PDF embeddings by specifying the folder location using the 'r' prefix. Store this data in a variable (e.g., data = EmbedPDF(r"D:\research_papers")).
4. When querying, input the query text and the variable containing the PDF vectors (e.g., QueryPDF("What is Self-Attention?", data)).
5. Ensure the PDF data is in a folder, 'r' is used when providing the file path, and vectors are stored in a variable during embedding.
6. Install any required dependencies using "pip install -r requirements.txt" in the terminal if needed.
