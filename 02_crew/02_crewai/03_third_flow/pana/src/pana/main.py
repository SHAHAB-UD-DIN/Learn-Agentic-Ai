from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv, find_dotenv
from pana.crews.teaching_crew.teaching_crew import TeachingCrew

_: bool = load_dotenv(find_dotenv())

class PanaFlow(Flow):

    @start()
    def generate_topic(self):
        response = completion(
            model= "gemini/gemini-1.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": "return the most trending topic in AI World. only share the topic no other text"
                }
            ]
        )
        self.state['topic'] = response['choices'][0]['message']['content']
        print(f"STEP 1 TOPIC: {self.state['topic']}")

    @listen("generate_topic")
    def generate_content(self):
        print(" STEP 2: Generating content...")
        result = TeachingCrew().crew().kickoff(
            inputs={
                "topic": self.state['topic']
            }
        )
        print(result)
        

def kickoff():
    obj = PanaFlow()
    obj.kickoff()