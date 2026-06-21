from google.adk.agents import Agent


analysis_agent = Agent(

    name="AnalysisAgent",

    model="gemini-2.0-flash",

    instruction="""

You analyze expense data.

Provide:

- Total spending
- Highest spending category
- Saving suggestions

"""

)