import validator

str1 = ["077123456",
"77 123-456",
"55 12 34 56",
"012345678",
"077 1234 56",
"091-123-4567",
"091  123456" ]

str2 = [
"email@example.com",
"firstname.lastname@example.com",
"email@subdomain.example.am",
"firstname+lastname@example.ru",
"1234567890@example.com",
"email@example.name",
"plainaddress",
"email@example",
"email.example.com",
"@example.com"
]

for i in str1:
    if validator.validate_phone_number(i):
        print(f"{i} is valid phone number")
    else:
        print(f"{i} is not valid phone number")
print()
for j in str2:
    if validator.validate_email(j):
        print(f"{j} is valid email")
    else:
        print(f"{j} is not valid email")