from crewai.flow import Flow, listen, start
from litellm import completion


class LitellmFlow(Flow):
    @start()
    def simple_flow(self):
        output = completion(
            model="gemini/gemini-2.0-flash",
            messages=[
                {
                    'role':'user',
                    'content':'who is the founder of pakistan?'
                }
            ])
        return output['choices'][0]['message']['content']
    
def run_flow():
    obj = LitellmFlow()
    result = obj.kickoff()
    print(result)