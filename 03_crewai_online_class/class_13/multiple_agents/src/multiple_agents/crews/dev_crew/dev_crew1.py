from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task



@CrewBase
class DevCrew:
    """Poem Crew"""


    @agent
    def junior_python_developer(self) -> Agent:
        return Agent(
            role="",
            goal="",
            backstory=""
        )
    
    @agent
    def senior_python_developer(self) -> Agent:
        return Agent(
            role="",
            goal="",
            backstory=""
        )

    @task
    def write_code(self) -> Task:
        return Task(
            description="",
            expected_output="",
            agent=
        )
    
    @task
    def review_code(self) -> Task:
        return Task(
            description="",
            expected_output="",
            agent=
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
