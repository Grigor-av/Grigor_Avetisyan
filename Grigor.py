def function(string):
    word = ""
    for i in set(string):
        word += i
    return word
print(function(input()))