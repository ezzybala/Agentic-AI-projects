from agents import Agent, function_tool
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from typing import Dict
import os
from dotenv import load_dotenv
load_dotenv(override=True)

@function_tool
def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
    """ Send out an email with the given subject and HTML body to all sales prospects """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("ezekiel.bala@outlook.com")  # Change to your verified sender
    to_email = To("ezzy.bala@gmail.com")  # Change to your recipient
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}


subject_instructions = "You can write a subject for a cold sales email. \
You are given a message and you need to write a subject for an email that is likely to get a response."

html_instructions = "You can convert a text email body to an HTML email body. \
You are given a text email body which might have some markdown \
and you need to convert it to an HTML email body with simple, clear, compelling layout and design."

subject_writer = Agent(name="Email subject writer", instructions=subject_instructions, model="gpt-4o-mini")
subject_tool = subject_writer.as_tool(tool_name="subject_writer", tool_description="Write a subject for a cold sales email")

html_converter = Agent(name="HTML email body converter", instructions=html_instructions, model="gpt-4o-mini")
html_tool = html_converter.as_tool(tool_name="html_converter",tool_description="Convert a text email body to an HTML email body")
# send_html_email('test email from sales agents', 'Welcome to agent world with sales agents')


email_tools = [subject_tool, html_tool, send_html_email]

instructions ="You are an email formatter and sender. You receive the body of an email to be sent. \
You first use the subject_writer tool to write a subject for the email, then use the html_converter tool to convert the body to HTML. \
Finally, you use the send_html_email tool to send the email with the subject and HTML body."


emailer_agent = Agent(
    name="Email Manager",
    instructions=instructions,
    tools=email_tools,
    model="gpt-4o-mini",
    handoff_description="Convert an email to HTML and send it")


handoffs = [emailer_agent]