# import json

# with open('./bayes.json') as f:
#     bayes = json.load(f)

# print(bayes)

import json

with open('/Users/cris/codeup-data-science/ds-methodologies-exercises/clustering/bayes.json') as f:
    bayes = json.load(f)

print(bayes)

# Write the code necessary to answer the following questions:
# Print out a message that gives the location of the class using the location and the floor properties.
bl = bayes["Location"]
bf = bayes["Floor"]

print(f"""
Location: {bl}
Floor No.: {bf}
""")

# If the class is active, print a message that says so.
active_status = bayes["isActive"]

print(active_status)

# Print out the number of students and number of instructors.
print(f"""
No. of Instructors: {len(bayes["Instructors"])}
No. of Students: {len(bayes["Students"])}""")

# Print out the name of the instructor that has the most favorite languages.

language_counter = []
for instructor in bayes["Instructors"]:
    language_counter.append(len(instructor["favoriteLanguages"]))
    max_lang = max(language_counter)
    if max_lang == len(instructor["favoriteLanguages"]):
        print(instructor["name"])

import pandas as pd

bayes_df = pd.DataFrame(bayes["Students"])
bayes_df

grades = bayes_df.examGrades.apply(pd.Series)
bayes_df.join(grades)

print(bayes["Instructors"])