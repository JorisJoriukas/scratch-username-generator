from random import randint
name = ['Apples', 'Bananas', 'Oranges', 'Cats', 'Dogs']
verb = ['Blue', 'Green', 'Red', 'Orange', 'Purple', 'Awesome', 'Epic', 'Deadly', 'Brave']
noun = [randint(1, 999)]
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked
while True:
     username = pick(verb),pick(name),pick(noun)
     print(username)
     print('Here\'s your username.')
     input(
    
