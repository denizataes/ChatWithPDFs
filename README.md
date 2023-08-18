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

# TR
1-PDF Belgelerini Yükleme:
Kullanıcı, Streamlit arayüzü üzerinden PDF belgelerini yükler.

2-PDF İçeriklerini Birleştirme:
Yüklenen PDF belgelerinin her biri okunarak içerikleri birleştirilir. Böylece tüm belgelerin metin içeriği tek bir büyük metin olarak elde edilir.

3-Metni Chunk'lara Ayırma:
Birleştirilen metin, belirli bir boyut ve örtüşme ile küçük parçalara (chunk) bölünür. Bu adım, uzun metinleri daha yönetilebilir parçalara bölmek için kullanılır.

4-Gömme (Embedding) ve Vektör Mağazası Oluşturma:
Chunk'lara ayrılan metin parçaları, metin gömme (embedding) yöntemi kullanılarak vektörler haline dönüştürülür. Bu gömme işlemi, metinlerin anlamsal temsillerini yakalamayı amaçlar. Bu vektörler, FAISS adlı bir vektör mağazasına eklenir. FAISS, vektörler arasında benzerlik aramalarını hızlı bir şekilde gerçekleştiren bir kütüphanedir.

5-Kullanıcı Sorusunu İşleme:
Kullanıcı, Streamlit arayüzü üzerinden bir soru sorar. Bu soru, sonraki adımlarda kullanılacak olan veri girdisidir.

6-Benzerlik Arama ve Cevap Alma:
Kullanıcının sorduğu soru, önceden oluşturulan vektör mağazasında benzer metinler aranarak en uygun cevapları bulmak için kullanılır. Bu benzerlik arama, özellikle kullanıcının sorduğu soruya benzer içeriğe sahip metin parçalarını belirlemeyi amaçlar. Daha sonra, bu benzer metin parçaları ve kullanıcının sorusu OpenAI API'sine gönderilir.

7-OpenAI API Kullanarak Cevap Alma:
Benzer metin parçaları ve kullanıcının sorusu OpenAI API'sine gönderilir. OpenAI, verilen metinlere dayalı olarak en iyi cevapları üretmeye çalışan bir yapay zeka modeli kullanır. Bu model, konuşma tabanlı ve doğal dil işleme yeteneklerine sahip olabilir. OpenAI, bu soruya dayalı olarak bir cevap üretir ve bunu geri döndürür.

8-Cevapları Görüntüleme:
OpenAI'den gelen cevaplar alındığında, bu cevaplar kullanıcının sorusuna yanıt olarak Streamlit arayüzünde görüntülenir. Kullanıcı ve bot (OpenAI) mesajları sırayla görüntülenir.

Bu şekilde, PDF belgelerin içeriği üzerinde benzerlik aramaları yaparak kullanıcının sorduğu sorulara uygun cevaplar bulan bir sohbet arayüzü oluşturulmuş olur.





