from google.adk.agents import LlmAgent
from google.adk.tools import google_search

def total_count_of_identity_access_management_iga_agents() -> dict:
    """Get the total count of identity access management (IGA) agents."""
    return {
        "total_identity": 100
    }


iga_assistance_agent = LlmAgent(
name="iga_assistance_agent",
model="gemini-2.5-flash",
description="A simple IGA assistant ",
instruction="""You are a friendly IGA assistant.
You can help answer user's generic questions on IGA and help plan their IGA goals. Be more friendly and positive.""",

tools=[total_count_of_identity_access_management_iga_agents]
# tools=[google_search] # allow to use google search tool to answer user's question
)


root_agent = iga_assistance_agent



# finance_assistance_agent = LlmAgent(
# name="finance_assistance_agent",
# model="gemini-2.5-flash",
# description="A simple finance assistant that helps with user's finance goals.",
# instruction="""You are a friendly finance assistant.
# You can help answer user's generic questions on finance and help plan
# their finance goals. Be more friendly and positive."""
# )


# root_agent = finance_assistance_agent