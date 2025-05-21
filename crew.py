from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from task import research_task,write_task



#now to call this into sequential order we will do use Crew Class...
crew = Crew(
    agents = [blog_researcher,blog_writer],
    tasks = [research_task,write_task],
    process=Process.sequential,
    memory = True,
    cache = True,
    max_rpm=100,
    share_crew=True
)

##lets start the task execution....process with enhanced feedback...
result = crew.kickoff(inputs={"topic":'AI vs ML vs DL vs Data Science - Difference Explained | Simplilearn'})
print(result)