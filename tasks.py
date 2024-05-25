from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def report_structurer_task(self, agent, meeting_context, meeting_objective):
        return Task(
            description=dedent(
                f"""\
                               Create and organize the structure of the report \
                                for the meeting using a SILAMIR GROUP like template. \
                                Incorporate section for all relevant details from the meeting\
                                to ensure a comprehensive and well-organized report. \
                                Meeting Context : {meeting_context}, \
                                Meeting Objectives : {meeting_objective}\ 
                                """
            ),
            expected_output=dedent(
                """\
                                   A organized and comprehensive meeting report structure following the SILAMIR template. \
                                   The report should cover sections over all essential points discussed during the meeting, \
                                   including action items, decisions made, and key takeaways."""
            ),
            agent=agent,
        )

    def meeting_notes_analyst_task(self, agent, meeting_context, meeting_objective):
        return Task(
            description=dedent(
                f"""\
                Analyze and organize the incomplete meeting notes to create a clear and concise narrative.
                Use your expertise and understanding of the SILAMIR report structure to identify missing pieces
                and arrange the information in a logical sequence. Your goal is to extract the crucial discussion points
                and present them as clear, actionable steps taken during the meeting.
                Meeting Context : {meeting_context}, \
                Meeting Objectives : {meeting_objective}\
                {self.__tip_section()}"""
            ),
            expected_output=dedent(
                """\
                A well-organized and clear narrative derived from the raw meeting notes. 
                The output should include all essential discussion points, key takeaways, and actionable steps,
                structured according to the SILAMIR report structure made by your coworker report structurer agent."""
            ),
            agent=agent,
        )

    def report_writer_task(self, agent):
        return Task(
            description=dedent(
                f"""\
                Craft a compelling and well-organized final report by integrating the structured framework
                provided by the Report Architect and the insightful analysis from the Meeting Notes Analyst.
                Use your exceptional writing skills to transform the complex information into a clear, concise, 
                and engaging narrative that resonates with the target audience. Ensure the final report adheres 
                to SILAMIR's high standards and effectively communicates the key points discussed during the meeting.
                {self.__tip_section()}"""
            ),
            expected_output=dedent(
                """\
                A polished, impactful, and well-organized final report that seamlessly weaves together the structured framework
                and the insightful analysis. The report should be clear, concise, and engaging, effectively communicating 
                the key points and adhering to SILAMIR's high standards."""
            ),
            agent=agent,
        )

    def report_qa_task(self, agent):
        return Task(
            description=dedent(
                f"""\
                Conduct a meticulous quality assurance review of the final report crafted by the Report Writer. 
                Verify factual accuracy, adherence to formatting and style guidelines, and overall clarity 
                for the intended audience. Ensure that the report meets SILAMIR's high standards for quality 
                and effectiveness. Identify any inconsistencies or areas for improvement and provide feedback 
                for necessary revisions.
                {self.__tip_section()}"""
            ),
            expected_output=dedent(
                """\
                A thoroughly reviewed final report with verified accuracy, adherence to guidelines, and clear communication 
                of key points with your Feedback and suggestions integrated in the final report for any necessary revisions 
                that should be provided to ensure the report 
                meets SILAMIR's high standards."""
            ),
            agent=agent,
        )
