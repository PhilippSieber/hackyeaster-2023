from faker import Faker
import random

faker = Faker()

# 10000 words, repeated
for i in range(1,10000):
    words = "_".join(faker.words(4))
    for i in range(1,random.randint(3,20)):
        print(f'he2023{{{words}}}')

# roughly 1000 words, appearing only once, but length != 
for i in range(1,1150):
    words = "_".join(faker.words(4))
    l = len(words)
    if l > 16 and l < 36 and l != 25:
        print(f'he2023{{{words}}}')