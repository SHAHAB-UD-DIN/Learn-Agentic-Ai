from crewai.flow import Flow, listen, start
from multiple_agents.crews.dev_crew.dev_crew1 import DevCrew

class DevCrewFlow(Flow):

    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff(
            inputs={
                "problem": "write python code for addition two numbers"
            }
        )
        return output.raw
    
def kickoff():
    dev_flow = DevCrewFlow()
    result = dev_flow.kickoff()
    print(result)