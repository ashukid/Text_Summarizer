import openai
import tiktoken
from time import time
from fastapi import UploadFile

from common.utils import break_up_file_to_chunks, read_text_from_file
from common.externals import openai_text_completion

async def consolidate_summary(prompt_response: str):
    print("\nConsolidating the summary for each chunk")
    start_time = time()
    prompt_request = "Consoloidate these meeting summaries in no less than 150 words and no more than 400 words : \n\n" + str(prompt_response)
    response = await openai_text_completion(prompt_request)
    end_time = time()
    print(f"Total time taken to consolidate summaries : {end_time-start_time} Seconds\n")
    return response["choices"][0]["text"]

async def get_summary(file: UploadFile):

    encoding = tiktoken.get_encoding("gpt2")
    chunks = break_up_file_to_chunks(file)

    instruction = "Given conversation happened between an interviewer and an interviewee. Summarise the details about the interviewee. Don't tell any details about the interviewers : \n\n"

    prompt_response = {}
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i} ")
        start_time = time()
        prompt_request = instruction + encoding.decode(chunks[i])
        response = await openai_text_completion(prompt_request)
        end_time = time()
        print(f"Total time taken to process chunk {i} : {end_time-start_time} Seconds")
        prompt_response[i] = response
    
    prompt_response_list = list(dict(sorted(prompt_response.items())).values())
    return await consolidate_summary(prompt_response_list)


