from mood_responses import mood_response
import text_utils
# Task 1: Your Mood Today

# Problem Statement: Create a Python program using a custom module holding a function that asks the user how they are feeling today and responds with a custom message based on the mood entered. This function should then be imported and used in another file "main.py".

# Expected Outcome: The program should be able to take a user's mood as input (e.g., happy, sad, excited) and return a corresponding custom message.

mood = input("How are you feeling today?: ")

message=mood_response(mood)

text_utils.reverse(mood)
text_utils.cap(mood)
text_utils.up_cased(mood)
