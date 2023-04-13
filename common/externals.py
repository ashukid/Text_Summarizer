import openai

from .config import settings
openai.api_key = settings.OPENAI_API_KEY

async def openai_text_completion(prompt: str):

    response =  await openai.Completion.acreate(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.6,
        max_tokens=256,
        top_p=0.6
    )

    return response
