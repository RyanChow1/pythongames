def feedback(word, c_l):
    display = "_" * len(word)
    display = list(display)
    for c in c_l:
        for s in range(len(word)):
            if c == word[s]:
                display[s] = c
    print(display)
feedback(word = "popeyes", c_l = "pe")