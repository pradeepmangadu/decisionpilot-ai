
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# 1. Initialize the language model
llm = ChatOpenAI(
    model="gpt-6-luna",
)

# 2. Define the decision analysis prompt
# This template gives the model its role and instructions, then inserts the
# user's decision into a separate message. The system instructions ask it to
# summarize the decision across six categories, avoid making up details, and
# call out unknowns; the final line asks for a concise, beginner-friendly reply.
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are DecisionPilot, an AI decision analysis assistant.

        Your job is to understand a user's decision
        and break it down clearly.

        Analyze the user's request and identify:

        1. Decision objective
        2. Budget or constraints
        3. Main requirements
        4. Important preferences
        5. Potential challenges
        6. Information that may be missing

        Do not invent facts.
        If information is missing, mention it.

        Keep your response concise and beginner-friendly.
        """
    ),
    (
        "human",
        "Analyze this decision:\n{decision}"
    )
])

# 3. Connect the prompt and model
decision_chain = prompt | llm

# 4. Get input from the user
user_decision = input(
    "What decision do you want help with?\n> "
)

# 5. Execute the chain
response = decision_chain.invoke({
    "decision": user_decision
})

# 6. Display the result
print("\n===== DECISIONPILOT ANALYSIS =====\n")
print(response.content)
