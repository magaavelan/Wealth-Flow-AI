import os
import logging
from typing import Optional
import google.generativeai as genai

logger = logging.getLogger(__name__)

def _get_api_key() -> str:
    """Securely retrieve the Gemini API key from environment variables."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
        
    if api_key in ("AIzaSyYourActualKeyGoesHere", "PASTE_YOUR_ACTUAL_AIZASY_KEY_HERE"):
        raise ValueError("GEMINI_API_KEY contains a placeholder value.")
    return api_key


def calculate_growth_projections(principal: float, annual_return: float, years: int) -> str:
    """Calculates future financial growth projections using compound interest."""
    try:
        p = float(principal)
        r = float(annual_return)
        y = int(years)
        
        rate_factor = 1.0 + (r / 100.0)
        compound_multiplier = rate_factor ** y
        
        future_value = p * compound_multiplier
        profit = future_value - p
        
        return f"After {y} years at an annual return rate of {r}%, your investment of ${p:,.2f} grows to ${future_value:,.2f} (Net Profit: ${profit:,.2f})."
    except Exception as e:
        return f"Calculation engine error: {str(e)}"


def query_ai_workflow(user_message: str, chat_history: Optional[list] = None) -> str:
    """Executes a synchronous conversation session with clean tool loop integration."""
    try:
        api_key = _get_api_key()
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            system_instruction=(
                "You are an advanced Enterprise AI Assistant built on Django. Be concise and professional. "
                "If a user asks for any numerical projection, savings forecast, or compounding interest calculation, "
                "always use your calculate_growth_projections tool to provide the answer."
            ),
            tools=[calculate_growth_projections]
        )
        
        # Format the historical turns into clean dictionaries that the legacy SDK natively reads
        formatted_history = []
        if chat_history:
            for msg in chat_history:
                role = "user" if msg.get("role") == "user" else "model"
                formatted_history.append({
                    "role": role,
                    "parts": [msg.get("content", "")]
                })
        
        # Start the chat session pre-loaded with the working history structure
        chat = model.start_chat(history=formatted_history)
        
        # Send the live user message
        response = chat.send_message(user_message)
        
        # Automatic tool execution check loop
        while response.function_calls:
            for function_call in response.function_calls:
                if function_call.name == "calculate_growth_projections":
                    args = function_call.args
                    
                    # Compute the local calculation tool results
                    tool_result = calculate_growth_projections(
                        principal=args.get("principal"),
                        annual_return=args.get("annual_return"),
                        years=args.get("years")
                    )
                    
                    # Return the tool answer to the model using a direct structured response dictionary
                    response = chat.send_message({
                        "parts": [{
                            "function_response": {
                                "name": function_call.name,
                                "response": {"result": tool_result}
                            }
                        }]
                    })
        
        return response.text
        
    except Exception as e:
        logger.error(f"Workflow failure: {e}")
        return f"System error occurred while building the AI workflow response: {str(e)}"