import base64
from dotenv import load_dotenv
# from openai import OpenAI
import os
import base64
from transformers import AutoProcessor, LlavaForConditionalGeneration
from PIL import Image
import torch
from pyexpat.errors import messages

load_dotenv()
def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")





# encoded_image = encode_image("acne.jpg")

query = "Is something wrong with my face?"
model="gpt-4o-mini"
def analyse_image_with_query(query,model,encoded_image):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=300
    )


    return response.choices[0].message.content
model_id = "llava-hf/llava-1.5-7b-hf"

processor = AutoProcessor.from_pretrained(model_id)
model = LlavaForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

def analyze_image(image, prompt):
    image = Image.open(image_path).convert("RGB")

    inputs = processor(
        text=prompt,
        images=image,
        return_tensors="pt"
    ).to(model.device)

    output = model.generate(
        **inputs,
        max_new_tokens=200
    )

    return processor.decode(output[0], skip_special_tokens=True)