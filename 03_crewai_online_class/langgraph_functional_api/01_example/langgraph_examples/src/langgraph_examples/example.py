import random
from typing import Literal, TypedDict, Dict, Any
from langgraph.func import entrypoint, task

# Define our types
class RouterOutput(TypedDict):
    route: Literal["math", "text", "code"]
    input: str

class Response(TypedDict):
    category: str
    input: str
    details: str
    output: str

class WorkflowOutput(TypedDict):
    result: Response
    route_taken: str

# Tasks for different routes
@task
def handle_math(input_text: str) -> Response:
    """Handle mathematical queries"""
    return {
        "category": "Mathematical Query",
        "input": input_text,
        "details": "Processing mathematical calculation...",
        "output": "This is a simulated math calculation result"
    }

@task
def handle_text(input_text: str) -> Response:
    """Handle text-based queries"""
    return {
        "category": "Text Analysis",
        "input": input_text,
        "details": "Analyzing text content...",
        "output": "This is a simulated text analysis result"
    }

@task
def handle_code(input_text: str) -> Response:
    """Handle code-related queries"""
    return {
        "category": "Code Processing",
        "input": input_text,
        "details": "Generating code solution...",
        "output": "This is a simulated code solution"
    }

# Router task
@task
def route_query(input_text: str) -> RouterOutput:
    """Route the query to appropriate handler"""
    route = random.choice(["math", "text", "code"])
    return {
        "route": route,
        "input": input_text
    }

# Main workflow
@entrypoint()
def workflow(input_text: str) -> WorkflowOutput:
    """Main workflow that routes and processes queries"""
    route_output = route_query(input_text).result()
    
    handlers = {
        "math": handle_math,
        "text": handle_text,
        "code": handle_code
    }
    
    handler = handlers[route_output["route"]]
    result = handler(route_output["input"]).result()
    
    return {
        "result": result,
        "route_taken": route_output["route"]
    }

def format_output(result: Dict[str, Any]) -> None:
    """Format and print the workflow output"""
    response = result["result"]
    print("\n" + "="*60)
    print(f"🔄 Route Selected: {result['route_taken'].upper()}")
    print("-"*60)
    print(f"📝 Category: {response['category']}")
    print(f"📥 Input: {response['input']}")
    print(f"🔍 Details: {response['details']}")
    print(f"📤 Output: {response['output']}")
    print("="*60)

def main():
    config = {
        "configurable": {
            "thread_id": "example_thread"
        }
    }

    test_inputs = [
        "What is 2+2?",
        "Explain what is Python",
        "Write a function to sort a list"
    ]
    
    print("\n🚀 Starting Router Pattern Demo")
    print("Each input will be randomly routed to a specialized handler\n")
    
    for input_query in test_inputs:
        result = workflow.invoke(input_query, config)
        format_output(result)

if __name__ == "__main__":
    main()


