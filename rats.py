'''r= int (input())
unit= int(input()) #amt of food rat consumesn = int(input())
x=[]
for i in range(n):
    y= int(input())
    x.append(y)

food = unit *r
need = 0

if not x:
    print(-1)
elif sum(x)<food:
    print("0")
else:
    houses = 0
    for i in range(n):
        need += x[i]
        houses += 1
        if need >=food:
            print(houses)
            break

'''
# Read the number of words
n = int(input().strip())

# Initialize a dictionary to count occurrences and a list to maintain order of appearance
word_count = {}
words_in_order = []

# Process each word
for _ in range(n):
    word = input().strip()
    # Add word to dictionary and list if it is new
    if word not in word_count:
        word_count[word] = 1
        words_in_order.append(word)
    else:
        word_count[word] += 1

# Output the number of distinct words
print(len(words_in_order))

# Output the count of each word in the order of its first appearance
print(" ".join(str(word_count[word]) for word in words_in_order))
