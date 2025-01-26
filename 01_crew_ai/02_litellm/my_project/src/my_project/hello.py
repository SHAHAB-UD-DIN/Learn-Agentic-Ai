from litellm import completion
import os

os.environ["GEMINI_API_KEY"] = "AIzaSyAcyACY-_PBKkjeMTZk4RMo0LQ61luDH5A"

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{ "content": "difference between liteLLm andlangchain","role": "user"}]
    )

    print(response)