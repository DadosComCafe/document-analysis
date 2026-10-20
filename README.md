# Document Analysis

# Sobre
O projeto possui como principal ideia a estruturação dos obtidos de fontes de dados não estruturados, utilizando para isso um __agente gemini__ e a tool __document-ai__, fornecida pela __GCP__.<br>
Este projeto visa explorar o uso do serviço [__document-ai__](https://docs.cloud.google.com/document-ai/docs/overview?hl=pt-br), usando-o como uma __tool__ dentro de um agente adk. O agente deve receber arquivos de vários formatos de imagem, texto, ou documentos, e gerar um __Json__, com as informações necessárias obtidas da análise deste arquivo/documento enviado.   

# Exemplo de Uso 
Por exemplo, você espera que o agente categorize notas fiscais, que podem vir em uma variedade de formatos (.xml, .jpg, .png, .pdf, .docx etc), e você possui um padrão de informações que quer obter. O que você deve fazer, é definir os campos os quais você quer informação do arquivo. Por exemplo em notas fiscais, quero de informações direta o nome da empresa, o nome do produto, o preço pago, de informações indiretas a classificação do produto, a usabilidade do produto. Sendo __informações diretas__ sendo obtidas puramente da extração do texto, e __informações indiretas__ através de uma análise ou processamento das __informações diretas__ extraídas do arquivo/documento.


![Logo](/images/logo.png)


# Como usar
1. Clone este repositório:
    - git clone https://github.com/DadosComCafe/document-analysis

2. Entre no diretório document_analysis_agent/, e edite a variável de ambiente
    - cd document_analysis
    - cd document_analysis_agent
    - Use o arquivo __env_sample.sh__ para criar o __env.sh__ 

3. Configure o ambiente python com o uv:
    - Dentro de __document_analysis_agent__, execute:
        - uv sync

4. Rode o arquivo .sh para exportar as variáveis de ambiente:
    - Dentro de __document_analysis_agent__, execute:
        - source env.sh

5. Rode o agente com o uv
    - Dentro de __document_analysis_agent__, execute:
        - uv run main.py
        
__OBS:__ Você necessita ter um projeto gcp previamente criado, com o vertex ativo. Em caso de dúvidas, use o seguinte repositório para guiá-lo:
- https://github.com/DadosComCafe/genai_gcp_study

# Configurar o Serviço DocumentAI da GCP
[Ativando, Configurando e Usando o DocumentAI](./document_analysis_agent/README.md)
