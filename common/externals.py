import openai

from .config import settings
openai.api_key = settings.OPENAI_API_KEY

async def openai_text_completion(prompt: str):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.7,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response
