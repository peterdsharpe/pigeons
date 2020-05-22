
# Write helper functions
line = lambda: print(40*"_","\n")

# Print title
print("""Tinder Pigeons
by Peter Sharpe""")
line()

# Gather data
print("Add someone to the database!")
name = input("\n\t1. Respondent name: ")
location = input("\n\t2. Location: ")
n_pigeons = input("\n\t3. How many pigeons could they carry: ")
contributor = input("\n\t4. Contributor name: ")
notes = input("\n\t5. Any other notes: ")
line()

# Load existing data, save to buffer, and write new data to disk.
with open("data.csv", "r") as f:
    data = f.readlines()
import copy
data_original = copy.copy(data)
data.append(
    "%s,%s,%f,%s,\"\"\"%s\"\"\"\n" %
    (name, location, float(n_pigeons), contributor, notes)
)
with open("data.csv", "w") as f:
    f.writelines(data)
print("New data added to data.csv!")
line()

# Run the pigeons script
print("Running the pigeons analysis script...")
import pigeons as p
if not input("Does the data look good? (y/n): ").lower().strip() == "y":
    print("Aborting and restoring old data!")
    with open("data.csv", "w") as f:
        f.writelines(data_original)
    exit(0)

# Run a Git commit to push up to the server
import os
cmds = [
    "git add .",
    "git commit -m \"Added new person: %s!\"" % name,
    "git push",
]
[os.system(cmd) for cmd in cmds]
