# Document Analysis

# Sobre
O projeto possui como principal ideia a estruturação dos obtidos de fontes de dados não estruturados, utilizando para isso um __agente gemini__ e a tool __document-ai__, fornecida pela __GCP__.<br>
Este projeto visa explorar o uso do serviço [__document-ai__](https://docs.cloud.google.com/document-ai/docs/overview?hl=pt-br), usando-o como uma __tool__ dentro de um agente adk. O agente deve receber arquivos de vários formatos de imagem, texto, ou documentos, e gerar um __Json__, com as informações necessárias obtidas da análise deste arquivo/documento enviado.   

# Exemplo de Uso 
Por exemplo, você espera que o agente categorize notas fiscais, que podem vir em uma variedade de formatos (.xml, .jpg, .png, .pdf, .docx etc), e você possui 