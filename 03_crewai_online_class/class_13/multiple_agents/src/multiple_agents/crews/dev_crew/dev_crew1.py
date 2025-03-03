from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task



@CrewBase
class DevCrew:
    """Poem Crew"""


    @agent
    def junior_python_developer(self) -> Agent:
        return Agent(
            role="junior python developer",
            goal="write python code solution without python type hints. for this problem '{problem}'",
            backstory="you have 3 years python web developement experience. you know how to use flask, django"
        )
    
    @agent
    def senior_python_developer(self) -> Agent:
        return Agent(
            role="senior python developer",
            goal="""review the python code generated by junior_python_developer for this problem '{problem}'
                    apply python type hints
                    apply pydocs
                    write pytest tests for the code""",
            backstory="""you have 20 years experence in machine learning, deep learning, generative ai, agentic ai.
                         you have good commands on crewai, langgraph and auto gent"""
        )

    @task
    def write_code(self) -> Task:
        return Task(
            description="write python solution with out python type hints and pydocs for this problems '{problem}'",
            expected_output="return python code only",
            agent=self.junior_python_developer
        )
    
    @task
    def review_code(self) -> Task:
        return Task(
            description="""you have toreview the python code generated by junior_python_developer for this problem '{problem}'
                           optimize the code.
                           apply python type hints
                           apply pydocs
                           write pytest tests for the code""",
            expected_output="return python code only",
            agent=self.senior_python_developer
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
