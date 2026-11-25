
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from schemas import DecisionAnalysis

load_dotenv()

# 1. Initialize the model
llm = ChatOpenAI(
    model="gpt-6-luna"
)

# 2. Connect the model with our Pydantic schema
structured_llm = llm.with_structured_output(
    DecisionAnalysis
)

# 3. Create the prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are DecisionPilot, an AI decision analyst.

        Analyze the user's decision.

        Extract:
        - Decision name
        - Objective
        - Budget
        - Requirements
        - Preferences
        - Constraints
        - Missing information

        Do not invent details.
        If information is not provided, use
        'Not specified' for budget and an empty
        list for other missing list fields.
        """
    ),
    (
        "human",
        "{user_decision}"
    )
])

# 4. Build the chain
decision_chain = prompt | structured_llm

# 5. Get user input
user_decision = input(
    "Enter your decision:\n> "
)

# 6. Invoke the chain
result = decision_chain.invoke({
    "user_decision": user_decision
})

# 7. Display structured output
print("\n===== DECISIONPILOT RESULT =====")

print(result.model_dump_json(indent=2))


print(type(result))
print(result.objective)
print(result.requirements)
print(result.budget)
print(result.decision)
print(result.missing_information)
