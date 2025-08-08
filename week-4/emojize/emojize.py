import re
import emoji

user = input("Input: ")
print("Output:", emoji.emojize(user, language="alias"))

# def main():
#     user = input("Input: ").strip()
#     matches = re.search(r"(^(:)(.+[\w])(:)$)", user)
#     if matches:
#         print(matches.group())

# Function that replaces the term with the suitable emoji
# def emoji_converter(term):
#     match term:
#         case ":thumbsup:" | ":thumbs_up:":
#             return "👍"

# main()
# Validate the string and detect the key term
# Retrieve the emoji associated with the key term
# Replace key term with emoji
