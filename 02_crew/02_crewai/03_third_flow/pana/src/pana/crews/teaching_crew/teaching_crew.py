from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class TeachingCrew(CrewBase):
    @agent
    def sir_zia(self):
        return Agent(
            role="Sir Zia",
            goal="You are a teacher who is teching a class about the benefits of learning Agentic AI",
            backstory="You are a teacher who is teaching a class about the benefits of learning Agentic AI",
        )
    
    @agent
    def sir_zia(self):
        return Agent(
            
        )
