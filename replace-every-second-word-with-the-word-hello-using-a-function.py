# https://stackoverflow.com/questions/47085552/replace-every-second-word-with-the-word-hello-using-a-function

def replace(sentence):

    l = sentence.split(' ')

    list_odd = l[0::2]
    print(list_odd)
    final_list = []

    for word in list_odd:
        final_list.append(word)
        final_list.append('hello')

    final_string = " ".join(final_list)

    print(final_string)
replace("I want to replace every other word in this string with hello")