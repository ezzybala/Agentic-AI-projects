from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool, OpenAIChatCompletionsModel, input_guardrail, GuardrailFunctionOutput
from openai import AsyncOpenAI
import asyncio
from sales_agent import get_sales_tools
from email_agent import handoffs, email_tools
from guardrail_agent import guardrail_agent, guardrail_against_name
import os
load_dotenv(override=True)

# sales_manager_instructions = """
# You are a Sales Manager at ComplAI. Your goal is to find the single best cold sales email using the sales_agent tools.
 
# Follow these steps carefully:
# 1. Generate Drafts: Use all three sales_agent tools to generate three different email drafts. Do not proceed until all three drafts are ready.
 
# 2. Evaluate and Select: Review the drafts and choose the single best email using your judgment of which one is most effective.
# You can use the tools multiple times if you're not satisfied with the results from the first try.
 
# 3. Handoff for Sending: Pass ONLY the winning email draft to the 'Email Manager' agent. The Email Manager will take care of formatting and sending.
 
# Crucial Rules:
# - You must use the sales agent tools to generate the drafts — do not write them yourself.
# - You must hand off exactly ONE email to the Email Manager — never more than one.
# """


# tools = get_sales_tools()

# sales_manager = Agent(
#     name="Sales Manager",
#     instructions=sales_manager_instructions,
#     tools=tools,
#     handoffs=handoffs,
#     model="gpt-4o-mini")

# message = "Send out a cold sales email addressed to Dear CEO from Alice"

# with trace("Automated SDR"):
#     result = await Runner.run(sales_manager, message)





async def main():
    # Initialize async OpenAI client
    client = AsyncOpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    # Get your sales tools
    tools = get_sales_tools()

    # Define Sales Manager agent
    sales_manager_instructions = """
    You are a Sales Manager at IntelliAutomate. Your goal is to find the single best cold sales email using the sales_agent tools.
    
    Follow these steps carefully:
    1. Generate Drafts: Use all three sales_agent tools to generate three different email drafts. Do not proceed until all three drafts are ready.
    
    2. Evaluate and Select: Review the drafts and choose the single best email using your judgment of which one is most effective.
    You can use the tools multiple times if you're not satisfied with the results from the first try.
    
    3. Handoff for Sending: Pass ONLY the winning email draft to the 'Email Manager' agent. The Email Manager will take care of formatting and sending.
    
    Crucial Rules:
    - You must use the sales agent tools to generate the drafts — do not write them yourself.
    - You must hand off exactly ONE email to the Email Manager — never more than one.
    """
    
    sales_manager = Agent(
        name="Sales Manager",
        instructions=sales_manager_instructions,
        tools=tools,
        handoffs=handoffs,
        model="gpt-4o-mini",  # or use model="gpt-4o-mini" in your Runner that uses AsyncOpenAI
        input_guardrails=[guardrail_against_name]
    )

    message = "Send out a cold sales email addressed to Dear CEO from Alice"

    with trace("Protected Automated SDRR"):
        # Runner.run is async so we await it
        result = await Runner.run(sales_manager, message)
        print(result)

# Run the async entrypoint
asyncio.run(main())