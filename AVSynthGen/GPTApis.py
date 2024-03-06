from openai import OpenAI

def CheckGPTConnection():
    print("checking")
    return 

def GetGPTResponse(prompt):
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    )
    #print(response['choices'][0]['message']['content'].strip())
    print(response)