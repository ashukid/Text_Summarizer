import tiktoken
from fastapi import UploadFile

def read_text_from_file(file: UploadFile):
    return file.file.read().decode()

def break_up_file_to_chunks(file: UploadFile, chunk_size: int = 2000, overlap: int = 100):

    text = read_text_from_file(file)

    encoding = tiktoken.get_encoding("gpt2")
    tokens = encoding.encode(text)
    num_tokens = len(tokens)
    
    chunks = []
    for i in range(0, num_tokens, chunk_size - overlap):
        chunk = tokens[i:i + chunk_size]
        chunks.append(chunk)
    
    return chunks