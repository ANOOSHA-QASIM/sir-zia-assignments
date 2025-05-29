print("Welcome to 'The Power of Small Steps' Story Game!")
print("Enter 3 simple inputs, and discover a story that will inspire you! \n")


name = input("Enter a name: ")
small_habit = input("Enter a small habit or action (e.g., reading one page, saving one rupee, exercising for 5 min): ")
big_goal = input("Enter a big goal (e.g., becoming successful, buying a house, becoming a leader): ")


story = f"""
{name} always dreamed of **{big_goal}**, but it seemed impossible.  
One day, someone told {name}:  
*"Great things start with small steps!"*  

So, {name} started **{small_habit}** every day.  
At first, it felt like nothing was changing... but slowly, everything started improving!  

Months passed, and {name} saw a huge difference. That small habit became a strong foundation.  
One day, {name} finally achieved **{big_goal}**!  

**Moral:** *Success is not about big actions; it's about small consistent steps!*
""" 

print("\nHere is your inspiring story!")
print(story)