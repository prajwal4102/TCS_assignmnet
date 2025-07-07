import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain

# Your Google API key
GOOGLE_API_KEY = "AIzaSyAKUDasjpMc_uui8Ny1PZxhR-JSI6QsG9E"

# Load the dataset
df = pd.read_csv("insurance_policies.csv", index_col="policy_id")
df["renewal_date"] = pd.to_datetime(df["renewal_date"]).dt.strftime("%d-%m-%Y")
print(df)

# Helper function to get policy details
def get_policy_details(policy_id):
    if policy_id not in df.index:
        return None
    row = df.loc[policy_id]
    return {
        "customer_name": row["customer_name"],
        "policy_type": row["policy_type"],
        "coverage_amount": row["coverage_amount"],
        "premium": row["premium"],
        "renewal_date": row["renewal_date"]
    }

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY
)

# Prompt with guardrails
prompt = PromptTemplate(
    input_variables=["user_question", "policy_info"],
    template="""
You are an insurance policy assistant. Answer customer questions using only the given policy data.

Policy Information:
{policy_info}

Customer Question:
{user_question}

Guardrails:
- Do NOT reveal personal info like customer name or contact details.
- If a question is out of scope (e.g., cancelation), reply: "Sorry, I can’t help with that. Please contact support."
- If policy ID is invalid, say: "Policy not found. Please verify your ID."
- If the question is ambiguous, ask for clarification.
- Always end with: "Please consult an insurance advisor for detailed guidance."

Answer:
"""
)

# Output parser
output_parser = StrOutputParser()

# LangChain LLM chain
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    output_parser=output_parser
)

# Chat function
def chat_with_bot(policy_id, user_question):
    policy_info = get_policy_details(policy_id)
    if not policy_info:
        return "Policy not found. Please verify your ID.\nPlease consult an insurance advisor for detailed guidance."
    
    policy_summary = f"Policy Type: {policy_info['policy_type']}, Coverage: ₹{policy_info['coverage_amount']}, Premium: ₹{policy_info['premium']}, Renewal Date: {policy_info['renewal_date']}"
    
    response = chain.run({
        "user_question": user_question,
        "policy_info": policy_summary
    })
    return response

# Example usage
if __name__ == "__main__":
    print(chat_with_bot("POL001", "What is my premium?"))
