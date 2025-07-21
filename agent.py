from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    openai_api_base="http://127.0.0.1:1234/v1",  
    openai_api_key="lm-studio",                 
    model="deepseek-coder-6.7b-instruct"         
)

def agent2_coder(task_request):
    print("[Agent 2] Generating code for the task...")
    response = llm([
        HumanMessage(
            content=f"Write a Python function for this task. Only return valid code, no explanation:\n{task_request}"
        )
    ])
    return response.content


def agent1_messenger(user_input):
    print("\n[Agent 1] Received user input.")
    coder_response = agent2_coder(user_input)
    print("[Agent 1] Sending code back to user.\n")
    return coder_response


if __name__ == "__main__":
    print("🤖 Two-Agent Python Code Generator (LangChain + Deepseek)\n")
    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() in ["exit", "quit"]:
            break
        final_output = agent1_messenger(user_prompt)
        print(f"\n💡 Code:\n{final_output}\n")
