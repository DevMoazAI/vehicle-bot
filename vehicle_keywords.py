# # vehicle_keywords.py
# import json
# import re
# from difflib import SequenceMatcher

# # Sample keywords – you can expand this later
# VEHICLE_KEYWORDS = [
#     "engine", "car", "bike", "motor", "gear", "battery", "tyre", "radiator",
#     "knocking", "heat", "coolant", "ac", "fuel", "oil", "noise", "brake",
#     "suspension", "check light", "dashboard", "milage", "vibration", "crank",
#     "puncture", "start nahi", "ignition", "mechanic", "biker", "auto", "scooter"
# ]

# def is_vehicle_related(text, threshold=0.7):
#     text_lower = text.lower()
#     for keyword in VEHICLE_KEYWORDS:
#         if keyword in text_lower:
#             return True
#         ratio = SequenceMatcher(None, text_lower, keyword).ratio()
#         if ratio > threshold:
#             return True
#     return False
