countdown_str = ""
for count in reversed(range(0,11)):
    countdown_str = countdown_str + str(count) + ", "
countdown_str = countdown_str + 'поехали!'
print(countdown_str)