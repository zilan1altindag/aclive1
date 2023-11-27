import itertools
import requests

base_url = "http://10.0.0.6/ctf_deploy/aclive/ddjS7HkE9M/A.php"
attributes = ["OSA", "OSB", "OSC", "HSA", "HSB", "HSD"]

output_file = "output.txt"

total_combinations = 2 ** len(attributes)

for combination in range(total_combinations):
    binary_combination = format(combination, f'0{len(attributes)}b')
    url = f"{base_url}?" + "&".join(f"{attr}={val}" for attr, val in zip(attributes, binary_combination))
    
    response = requests.get(url).text
    
    if "Flag" in response:
        print(f"Found a combination that satisfies the policy: {url}")
        with open(output_file, "a") as file:
            file.write(url + "\n")
        break

print("No combination found.")
