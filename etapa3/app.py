import torch
from transformers import pipeline, GenerationConfig

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    dtype=torch.bfloat16,
    device=device,
    clean_up_tokenization_spaces=False,
)

pipe.model.generation_config.max_length = None

generation_config = GenerationConfig(
    max_new_tokens=50,
    do_sample=True,
    temperature=1.0,
    top_k=1000,
    top_p=0.1
)	

system_prompt = "You are a helpful assistant."
user_prompt = "Explain what a neural network is."

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
]

prompt = pipe.tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True, 
)

predictions = pipe(
    prompt,
    max_length=None,
    generation_config=generation_config,
    return_full_text=False
)
print(predictions)



