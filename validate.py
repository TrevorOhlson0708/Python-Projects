import re

email = input("Whats your email? ").strip()

if re.search(r"^\w.+@(\w.+\.)?\w+\.edu$",email, re.IGNORECASE):
    print("Valid")
else: 
    print("Invalid")