from openai import OpenAI


client = OpenAI(
    api_key="YOUR_API_KEY"
)


question = input(
    "Ask your AI Study Assistant: "
)


response = client.chat.completions.create(

    model="gpt-4.1-mini",

    messages=[
        {
            "role":"system",
            "content":
            "You are a helpful AI tutor."
        },

        {
            "role":"user",
            "content":question
        }
    ]

)


answer = response.choices[0].message.content


print("\nAI Tutor Response:")
print(answer)
