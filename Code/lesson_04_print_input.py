# Business prompt Builder
name = input("Your name: ")
business = input("Business type: ")
problem = input("Biggest problem: ")

budget = int(input("Monthly budget (PKR): "))

print()
print(f"Welcome, {name}!")
print("--- Your AI Prompt ---")

prompt = (
    f"Suggest 3 AI solutions for a {business} that struggles with {problem}. "
    f"Budget: {budget} PKR per month."
)
print(prompt)