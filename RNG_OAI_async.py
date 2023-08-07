import asyncio
import os
import openai
import tiktoken
import openai_async

with open('secretkey.txt', 'r') as f:
    secret = f.readline()

low=0
high=5
samples=10

enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
possible_nums=range(low,high+1) # int from 1 to 10
possible_tokens = {f"{enc.encode(f'{i}')[0]}": 100 for i in possible_nums} #coerces model to generate a number from 1 to 10

async def generateRating(metrics):
    completion = await openai_async.chat_complete(
        secret,
        timeout=60,
        payload={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"generate a random number from {str(low)} to {(high)}"}],
            "temperature": 0.7,
            "max_tokens": 1,
            "logit_bias": possible_tokens

        },
    )
    # print(completion.json())
    res = completion.json()['choices'][0]['message']['content']
    res = res.strip().lower()
    return res

async def run_concurrent_calls():
    # Number of concurrent calls
    num_concurrent_calls = samples #eventually replace with a semaphore to limit the number of concurrent calls

    # List to store the coroutines
    tasks = []

    for i in range(num_concurrent_calls):
        task = generateRating(metrics=[])
        tasks.append(task)

    # Run the coroutines concurrently
    results = await asyncio.gather(*tasks)

    # Print or process the results as needed
    print(results)

if __name__ == "__main__":
    # Setup asyncio event loop
    loop = asyncio.get_event_loop()

    # Run the concurrent calls function
    loop.run_until_complete(run_concurrent_calls())