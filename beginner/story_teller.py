# starter project

def get_input(word_type: str) -> str:
    user_input = input(word_type)
    return user_input

noun = get_input("noun: ")
verb = get_input("verb - present tense: ")
noun2 = get_input("noun: ")
verb2 = get_input("verb - present tense: ")

story = f"""
Once upon a time, there was a {noun} who loved to {verb} all day.

Onde day, {noun2} walked into the room and caught the {noun} in the act.

{noun2}: "What are you doing?"
{noun}: "I'm just {verb}ing, what's the big deal?"
{noun2}: "Well, it's not every day that you see a {noun} {verb}ing in the middle of the day."
{noun}: "I guess you're right. Maybe I should take a break"
{noun2}: "That's probably a good idea. Why don't we go {verb2} instead?"
{noun}: "Sure, that sounds like fun!"

And so, {noun2} and the {noun} went off to {verb2} and had a great time.
The end.

"""

print(story)
