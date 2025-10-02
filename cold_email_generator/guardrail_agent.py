from agents import Agent, input_guardrail, Runner, GuardrailFunctionOutput
from pydantic import BaseModel


class phone_number_CheckOutput(BaseModel):
    is_phone_in_message: bool
    phone_number: str

guardrail_agent = Agent( 
    name="Name check",
    instructions="Check if the user is including someone's phone number in what they want you to do.",
    output_type=phone_number_CheckOutput,
    model="gpt-4o-mini"
)

@input_guardrail
async def guardrail_against_name(ctx, agent, message):
    result = await Runner.run(guardrail_agent, message, context=ctx.context)
    is_phone_in_message = result.final_output.is_phone_in_message
    return GuardrailFunctionOutput(output_info={"found_phone_number": result.final_output},tripwire_triggered=is_phone_in_message)