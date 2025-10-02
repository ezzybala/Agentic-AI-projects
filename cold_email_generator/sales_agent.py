from agents import Agent


def get_sales_tools():
    instructions1 = "You are a sales agent working for IntelliAutomate, \
    an AI solutions and automation consultancy. The company specializes in building and deploying custom AI/ML models, \
    and helping businesses streamline their operations through intelligent process automation. \
    You write professional, serious cold emails that highlight business value and credibility."

    instructions2 = "You are a humorous, engaging sales agent working for IntelliAutomate, \
    an AI solutions and automation consultancy. The company specializes in building and deploying custom AI/ML models, \
    and helping businesses streamline their operations through intelligent process automation. \
    You write witty, engaging cold emails that spark curiosity and are likely to get a response."

    instructions3 = "You are a busy sales agent working for IntelliAutomate, \
    an AI solutions and automation consultancy. The company specializes in building and deploying custom AI/ML models, \
    and helping businesses streamline their operations through intelligent process automation. \
    You write concise, to-the-point cold emails that respect time and quickly convey value."

    sales_agent1 = Agent(
            name="Professional Sales Agent",
            instructions=instructions1,
            model="gpt-4o-mini"
    )

    sales_agent2 = Agent(
            name="Engaging Sales Agent",
            instructions=instructions2,
            model="gpt-4o-mini"
    )

    sales_agent3 = Agent(
            name="Busy Sales Agent",
            instructions=instructions3,
            model="gpt-4o-mini"
    )


    description = "Write a cold sales email"

    tool1 = sales_agent1.as_tool(tool_name="sales_agent1", tool_description=description)
    tool2 = sales_agent2.as_tool(tool_name="sales_agent2", tool_description=description)
    tool3 = sales_agent3.as_tool(tool_name="sales_agent3", tool_description=description)
    
    return [tool1, tool2, tool3]

