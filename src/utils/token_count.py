import os
import tiktoken



def token_count(messages, model="gpt-3.5-turbo-0125"):  
    encoding = tiktoken.encoding_for_model('gpt-3.5-turbo-0125')
    # if model == "gpt-3.5-turbo" or model == "gpt" or model == "gpt-35-instant":
    #     # print("Warning: gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301.")
    #     return token_count(messages, model="gpt-3.5-turbo-0301")
    # elif model == "gpt-4":
    #     # print("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
    #     return token_count(messages, model="gpt-4-0314")

    # if "gpt-3.5" in model:
    #     # every message follows <|start|>{role/name}\n{content}<|end|>\n
    #     tokens_per_message = 4
    #     tokens_per_name = -1  # if there's a name, the role is omitted
    # elif "gpt-4" in model:
        # tokens_per_message = 3
        # tokens_per_name = 1
    # else:
    #     raise NotImplementedError(
    #         f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")

    tokens_per_message = 4
    tokens_per_name = 1

    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens


def calculate_openai_cost(num_input_tokens, num_output_tokens):
    """
    Calculates the cost for the GPT-3.5-Turbo-0125 model based on the number of input and output tokens.

    Args:
        num_input_tokens (int): The number of input tokens.
        num_output_tokens (int): The number of output tokens.

    Returns:
        float: The cost in dollars.
    """
    num_input_tokens = num_input_tokens / 1000000
    num_output_tokens = num_output_tokens / 1000000

    cost = num_input_tokens * 0.5 + num_output_tokens * 1.5

    # Save the cost as an environment variable
    if 'OPENAI_COST' in os.environ and os.environ['OPENAI_COST'].strip():
        # If it is set and not empty, update its value
        os.environ['OPENAI_COST'] = str(float(os.environ['OPENAI_COST']) + cost)
    else:
        # If it is not set or is empty, set it to the current 'cost'
        os.environ['OPENAI_COST'] = str(cost)
    print('os.environ["OPENAI_COST"]:', os.environ["OPENAI_COST"])
    return cost