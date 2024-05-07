from replicate.client import Client
import os


# Takes a series of reviews and a model name
def get_summary(reviews, model, key):
    replicate = Client(api_token=key)
    init_sum = []
    for review in reviews:
    # The meta/meta-llama-3-70b-instruct model can stream output as it's running.
        msg = ""
        for event in replicate.stream(
            model,
            input={
                "top_k": 50,
                "top_p": 0.9,
                "prompt": f"Here is a product review: {review}\n The principal like or disklike in the review is",
                "max_tokens": 512,
                "min_tokens": 10,
                "temperature": 0.6,
                "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou summarize reviews by returning the principal complaint or praise.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
                "presence_penalty": 1.15,
                "frequency_penalty": 0.2
            },
        ):
            msg+=str(event)
        init_sum.append(msg)


    reworded_revs = ""
    for rev in init_sum:
        reworded_revs += f"Review: {rev}\n"
    msg = ""
    for event in replicate.stream(
        model,
        input={
            "top_k": 50,
            "top_p": 0.9,
            "prompt": f"Consider these reviews:\n{reworded_revs} By combining similar reviews, we see that ",
            "max_tokens": 512,
            "min_tokens": 0,
            "temperature": 0.6,
            "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou return text in a markdown format. You summarize reviews by consolidating similar reviews, returning the most common reviews first, and sharing how many times that review appeared. Each review must be returned either by itself or consolidated with others. The total number of reviews in the summary should be equal to the number of reviews you receive. Don't reference specific reviews. Don't write anything after the bulleted summary. Your goal is to be helpful to someone who wants to know a product's potential issues. You start by saying: 'Here is a summary of the reviews:'<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
            "presence_penalty": 1.15,
            "frequency_penalty": 0.2
        },
    ):
        msg+=str(event)
    return msg