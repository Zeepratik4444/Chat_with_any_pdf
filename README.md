# Chat_with_any_pdf
Upload File and chat with pdf

Welcome to Chat with PDF Project made by Pratik Kumar

In this project i have integrated LLM models to work with PDF and get data out of it with the help of these Language Models

I have created a script so that we can import these in jupyter notebooks and get the data out.

We will be doing so in two process:
1. We will feed the model the pdf we want to chat with and get more information in less complex language
2. We will then ask our query and also the model name so that we can make sure we are querying the right pdf file.

The process is simple and as following:
1. we will save the file and save the data in the folder research_papers.
2. We will move forward by giving command "from read_pdf import import EmbedPDF,QueryPDF
3. We need to feed the model the folder the pdf is in. example :data= EmbedPDF(r"D:\research_papers").
4. Please make sure to mention the r before the file path, it will make sure this is a raw string and also please store the data in a varriable.
5. To query the pdf we will be mentioning the Query in plain text and also the varriable we have stored our pdf vectors in. Example: QueuryPDF("What is Self-Attention?",data)
6. The above command will help us in retrieving the data we need from pdf file.


Things to keep in mind before getting started:
- The data must be stored in a folder 
- While giving the EmbedPDF command we need to mention "r" before feeding the path 
- There must be a varriable storing the vectors we have got from embedding the pdf
- While querying we need to mention the same varriable the vectors are stored in so that it retireive the vectors


I have attached a Jupyter notebook demonstrating how to query the pdf named test.ipynb
