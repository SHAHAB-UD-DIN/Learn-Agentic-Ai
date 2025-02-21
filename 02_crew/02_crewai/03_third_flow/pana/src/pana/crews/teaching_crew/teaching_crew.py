from crewai import Agent, Task, Crew
from crewai.project import CrewBase
from loguru import logger


class TeachingCrew:
    def sir_zia(self) -> Agent:
        logger.info("Creating Sir Zia agent")
        return Agent(
           role="Sir Zia",
           goal="You are a teacher who is teaching a topic to a student",
           backstory="You are a teacher who is teaching a topic to a student",
           llm="gemini/gemini-1.5-flash",
           verbose=True
        )

    def describe_topic(self) -> Task:
        logger.info("Describing topic")
        return Task(
            description="describe {topic} in detail. Provide a detailed explanation of the topic.",
            expected_output="A detailed description of {topic} with examples and real-life applications.",
            agent=self.sir_zia(),
            verbose=True
        )

    def crew(self) -> Crew:
        return Crew(
            agents=[self.sir_zia()],
            tasks=[self.describe_topic()],
            verbose=True
        )
