print("Hello")
print('Hello')
#No difference

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Ok

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#ALso ok

a = "Hello, World!"
print(a[1])
#e

for x in "banana":
  print(x)
'''
b
a
n
a
n
a
'''

a = "Hello, World!"
print(len(a))
#13

txt = "The best things in life are free!"
print("free" in txt)
#True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#Yes, 'free' is present.

txt = "The best things in life are free!"
print("expensive" not in txt)
#True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#No, 'expensive' is NOT present.