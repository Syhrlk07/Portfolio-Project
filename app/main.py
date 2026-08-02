print("===============================")
print("       Kiki Research AI")
print("===============================")
print("Knowledge Base is starting...")
project_name = "=== Kiki Research AI ==="

print(project_name)


import os

folder = "research"

folders = os.listdir(folder)

print("Folders found:\n")

for folder in folders:
    print("-", folder)