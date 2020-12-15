def main():
    word_occurrences={}
    text = input('Please input a text:\n')
    words = text.split()
    for word in words:
        if word in word_occurrences.keys():
            word_occurrences[word] = word_occurrences[word] + 1
        else:
            word_occurrences[word] = 1

    word_list = list(word_occurrences.keys())
    length = max(len(word) for word in word_list)
    word_list.sort()

    for word in word_list:
        print('{:{}}: {}'.format(word,length,word_occurrences[word]))

main()

















