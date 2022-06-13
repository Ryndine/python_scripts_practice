#! python3

import re, pyperclip

with open('')

# Phone regex
phoneRegex = re.compile(r'''
# 000-000-0000, 000-0000, (000) 000-0000, 000-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?	# area code (optional)
(\s|-)						#first separator
\d\d\d						#first 3 digits
-							#separator
\d\d\d\d					#last 4 digits
(((ext(\.)?\s)|x)			# extension word (optional)
 (\d{2,5}))?
) # extension number (optional)
''', re.VERBOSE)

# Email regex
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+		# name part
@		# @ symbol
[a-zA-Z0-9_.+]+		# domain name part
''', re.VERBOSE)

# Clipboard text
text = pyperclip.paste()

# Extract phone/email
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedEmail)

# print(extractedPhone)
# print(extractedEmail)

# allPhoneNumbers = []
# for phoneNumber in extractedPhone:
#     scraped_info = {}
#     scraped_info['number'] = phoneNumber[0]
# 	allPhoneNumbers.append(scraped_info)

# # Copy to clipboard
# results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)'
# pyperclip.copy(results)
