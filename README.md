# ChatWithPDFs
Chatting with multiple pdfs
## How It Works
The MultiPDF Chat App is a Python application that allows you to chat with multiple PDF documents. 
You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries.

<img src="https://github.com/denizataes/SeansSwiftUI/assets/85442526/ebc8356f-e1d7-453c-a7b8-371a2f8da8d6" width="1100" height="580">

The application follows these steps to provide responses to your questions:

* PDF Loading: The app reads multiple PDF documents and extracts their text content.

* Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

* Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

* Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

* Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

