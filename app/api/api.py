from api.pdf_q_a import PdfQA


def pdf_to_qna(payload):
    # Initialize PDFQA
    config = {"persist_directory":None,
          "load_in_8bit":False,
          "embedding" : payload['embedding_name'],
          "llm":payload['model_name'],
          "pdf_path":payload['file_location']
          }
    pdfqa = PdfQA(config=config)
    pdfqa.init_embeddings()
    pdfqa.init_models()

    # Create Vector DB 
    pdfqa.vector_db_pdf()

    # Set up Retrieval QA Chain
    pdfqa.retreival_qa_chain()

    # Query the model
    final=pdfqa.answer_query(payload['question'])
    return final