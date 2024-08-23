import re

# Find all email addresses and dates in the given text

text = "On 01-8-2024, the project manager, Sarah Jenkins, reached out to the team via email to confirm the final deadline for the delivery of the project. She stated in her email sent to sarah.jenkins@techsolutions.com that all deliverables must be submitted by 21/12/2024. Additionally,she reminded the team to send any project updates to updates@techsolutions.com and to CC her personalemail, sarah.j.dev@gmail.com, if there were any issues along the way 8-3/2034."

# Corrected regex pattern for finding dates

# pattern = r"\b(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}\b"

# pattern = r"\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b"

# jenkins@techsolutions.com
# updates@techsolutions.com
# sarah.j.dev@gmail.com

pattern = r"[a-zA-Z.]+\@[a-zA-Z.]+\.[a-zA-Z.]+"

# Find all dates

# dates = re.findall(pattern,text)
# print(dates)

# Find all emails

# emails = re.findall(pattern,text)
# print(emails)

txt = "The rain in Spain"

# x = re.findall("ai",txt)
# print(x)

# x = re.findall("Portugal",txt)
# print(x)

# x = re.search("\s",txt)
# print("The first white-space character is located in position : ",x.start())

# x = re.split("\s",txt)
# print(x)

# x = re.split("\s",txt,1)
# print(x)

# x = re.sub("\s","9",txt)
# print(x)

# x = re.sub("\s","9",txt,2)
# print(x)

# x = re.search(r"\bS\w+",txt)
# print(x.group())



