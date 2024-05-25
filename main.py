import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

load_dotenv()

tasks = CustomTasks()
agents = CustomAgents()

print("## Welcome to the Meeting Report Crew")
print("-------------------------------")
meeting_context = input("What is the context of the meeting?\n")
meeting_objective = input("What is your objective for this meeting?\n")

# Create Agents
report_structurer_agent = agents.report_structurer_agent()
meeting_notes_analyst_agent = agents.meeting_notes_analyst()
report_writer_agent = agents.report_writer_agent()
report_qa_agent = agents.report_qa_agent()

# Create Tasks
create_report_structure = tasks.meeting_notes_analyst_task(
    report_structurer_agent, meeting_context, meeting_objective
)
analyse_notes = tasks.meeting_notes_analyst(
    meeting_notes_analyst_agent, meeting_context, meeting_objective
)
write_report = tasks.report_writer_task(report_writer_agent)
final_report_qa = tasks.report_qa_task(report_qa_agent)

analyse_notes.context = [create_report_structure]
write_report.context = [create_report_structure, analyse_notes]
final_report_qa.context = [write_report]


# Create Crew responsible for Copy
crew = Crew(
    agents=[
        report_structurer_agent,
        meeting_notes_analyst_agent,
        report_writer_agent,
        report_qa_agent,
    ],
    tasks=[create_report_structure, analyse_notes, write_report, final_report_qa],
)

report_generation = crew.kickoff()


# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(report_generation)
