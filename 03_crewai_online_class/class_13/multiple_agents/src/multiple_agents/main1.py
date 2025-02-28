from crewai import Flow, start, listen
from multiple_agents.crews.dev_crew.dev_crew import DevCrew

class DevCrew(Flow):

    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff(
            input={
                "problem":"write python code for addition two numbers"
            }
        )
        return output.raw
    
def kickoff():
    obj = DevCrew()
    result = obj.kickoff()
    print(result)