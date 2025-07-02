# app_logic.py
# from vehicle_keywords import is_vehicle_related
from llm.llm_query import get_response_from_llm

def handle_user_query(user_input):
    # Let the LLM and system prompt handle all filtering and relevance
    response = get_response_from_llm(user_input)
    return response




# Professional Auto Mechanic Assistant - System Prompt

# **FILE FORMAT: .txt or .md**
# **USAGE: Copy this entire prompt and use as system prompt for your LLM**
# **VERSION: Production v1.0**







# ## Implementation Notes:
# - **File Format**: Save as .txt or .md file
# - **Token Count**: Approximately 1,200 tokens
# - **Compatible with**: GPT-4, Claude, Gemini, and other modern LLMs
# - **Update Frequency**: Review monthly for accuracy
# - **Deployment**: Use as system prompt in your application

# ## Quick Start:
# 1. Copy the entire prompt above
# 2. Paste into your LLM's system prompt field
# 3. Test with sample queries
# 4. Adjust regional pricing/vehicle data as needed