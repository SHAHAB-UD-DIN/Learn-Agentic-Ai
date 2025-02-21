from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv, find_dotenv
_: bool = load_dotenv(find_dotenv())

class PanaFlow(Flow):

    @start()
    def generate_topic(self):
        response = completion(
            model= "gemini/gemini-1.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": "return the most trending topic in AI World. only share the topic, no other text"
                }
            ]
        )
        self.state['topic'] = response['choices'][0]['message']['content']
        print(f"STEP 1 TOPIC: {self.state['topic']}")

def kickoff():
    obj = PanaFlow()
    obj.kickoff()