
# str_methods
# Demonstrating all str methods with examples

s = "hello"
print(s.capitalize())  # 1. capitalize() - Output: "Hello"

s = "HELLO"
print(s.casefold())  # 2. casefold() - Output: "hello"

s = "hello"
print(s.center(10, '-'))  # 3. center() - Output: "--hello---"

s = "banana"
print(s.count('a'))  # 4. count() - Output: 3

s = "hello"
encoded_s = s.encode("utf-8")
print(encoded_s)  # 5. encode() - Output: b'hello'

s = "hello"
print(s.endswith("o"))  # 6. endswith() - Output: True

s = "hello\tworld"
print(s.expandtabs(4))  # 7. expandtabs() - Output: "hello   world"

s = "hello"
print(s.find('e'))  # 8. find() - Output: 1

s = "Hello, {}!"
print(s.format("Kenijan"))  # 9. format() - Output: "Hello, Kenijan!"

d = {'name': 'Kenijan'}
print("Hello, {name}!".format_map(d))  # 10. format_map() - Output: "Hello, Kenijan!"

s = "hello"
print(s.index('e'))  # 11. index() - Output: 1

s = "hello123"
print(s.isalnum())  # 12. isalnum() - Output: True

s = "hello"
print(s.isalpha())  # 13. isalpha() - Output: True

s = "123"
print(s.isdigit())  # 14. isdigit() - Output: True

s = "hello"
print(s.islower())  # 15. islower() - Output: True

s = "123"
print(s.isnumeric())  # 16. isnumeric() - Output: True

s = "   "
print(s.isspace())  # 17. isspace() - Output: True

s = "HELLO"
print(s.isupper())  # 18. isupper() - Output: True

s = "-"
print(s.join(["a", "b", "c"]))  # 19. join() - Output: "a-b-c"

s = "hello"
print(s.ljust(10, '-'))  # 20. ljust() - Output: "hello-----"

s = "HELLO"
print(s.lower())  # 21. lower() - Output: "hello"

s = "   hello"
print(s.lstrip())  # 22. lstrip() - Output: "hello"

s = "hello world"
print(s.partition(" "))  # 23. partition() - Output: ('hello', ' ', 'world')

s = "hello"
print(s.replace("h", "H"))  # 24. replace() - Output: "Hello"

s = "hello"
print(s.rfind('l'))  # 25. rfind() - Output: 3

s = "hello"
print(s.rjust(10, '-'))  # 26. rjust() - Output: "-----hello"

s = "a-b-c"
print(s.rsplit("-"))  # 27. rsplit() - Output: ['a', 'b', 'c']

s = "hello   "
print(s.rstrip())  # 28. rstrip() - Output: "hello"

s = "a-b-c"
print(s.split("-"))  # 29. split() - Output: ['a', 'b', 'c']

s = "hello"
print(s.startswith("he"))  # 30. startswith() - Output: True

s = "   hello   "
print(s.strip())  # 31. strip() - Output: "hello"

s = "hello world"
print(s.title())  # 32. title() - Output: "Hello World"

s = "hello"
print(s.upper())  # 33. upper() - Output: "HELLO"

s = "42"
print(s.zfill(5))  # 34. zfill() - Output: "00042"


