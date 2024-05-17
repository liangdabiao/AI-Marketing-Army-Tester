# from openai import OpenAI
import openai
import instructor
 

client = openai.Client(api_key="sk-JXLXW5xPfdTC0QyuTHyutTYsDA8D7YgYx2AHwWgyRfd9sB",base_url="https://api.chatanywhere.com.cn/v1/")

import instructor
instructor.patch(client)

def analyze_image_basic(image_url, prompt):
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {
            "type": "image_url",
            "image_url": {
                "url": image_url,
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    return response.choices[0].message.content



def generate_with_response_model(user_prompt,response_model):

    resut: response_model = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_model=response_model,
        messages=[{"role": "user", "content": user_prompt}]
    )

    return resut




