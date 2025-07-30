# For Loop : Finite Looping

# Example 1 : 
for i in range(5):
    print("Hello")
    
# Example 2 : 
names: list[str] = ["Amith", "Sidvin", "Varun", "Akram"]

for name in names:
    print(f"Hello, {name}")
    
# While Loop : Infinite Looping

# Example 1 : 
i: int = 0
while i < 5:
    print(f'number : {i}')
    i += 1