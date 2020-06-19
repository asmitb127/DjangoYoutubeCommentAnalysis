import re

# it finds the regular exoresssion matching the pattern

dictionay = {}
# comment_list = ['Hello My Name Is Asmit',
#                 'Hello He Is Krishna', 'Hello How Are You', 'Good Video', 'Good One', 'Hello World', 'This is the most beatiful program that i have written', 'Data science is the sexist job of 21st century', 'Blockchain is the sexist job of 22nd century']
sorted_most_freq = []
sorted_lest_freq = []


# def __init__():
#     pass


def get_most_frequent():
    if sorted_most_freq:
        return sorted_most_freq
    else:
        print("Empty sorted_most_freq")


def get_least_frequent():
    if sorted_lest_freq:
        return sorted_lest_freq
    else:
        print("Empty sorted_lest_freq")


# it finds the match regex


def match_re_find(test_patterns, test_phrase):
    for test in test_patterns:
        print("searhing for pattern {}".format(test))
        words = re.findall(test, test_phrase)
        print('\n')
        return words

# it passes the individual comments to the slicing_comment function


def slice_comments(comment_list):
    for comment in comment_list:
        slicing_comment(comment)
    sorted_comment_list = sorted(
        dictionay.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, 20):
        sorted_most_freq.append(sorted_comment_list[i])
    for i in range(sorted_comment_list.__len__()-10, sorted_comment_list.__len__()):
        sorted_lest_freq.append(sorted_comment_list[i])

# it slices the comments for finding the regular expression


def slicing_comment(comment):
    test_pattern1 = [r'\D+']
    string = match_re_find(
        test_pattern1, comment)
    test_pattern2 = [r'\w+']
    my_string = ' '.join(string)
    required_string = match_re_find(test_pattern2, my_string)

    # print(required_string)
    # test_pattern = ['[^ ]+']
    # words = match_re_find(test_pattern, comment)
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    # no_emoji_string = match_re_find(emoji_pattern, ' '.join(required_string))
    # no_emoji_string = emoji_pattern.sub(r'', ' '.join(required_string))
    final_string = emoji_pattern.sub(
        r'', ' '.join(required_string))  # no emoji
    final_comment_list = match_re_find(['[^ ]+'], final_string.lower())
    count_comment(final_comment_list)


neutral_words = ["the", "and", "a", "that", "I", "it", "not", "he", "as", "you", "this", "but", "his", "they", "her", "she",
                 "or", "an", "will", "more", "video", "only", "like", "my", "one", "all", "would", "there", "their", "to", "of", "in", "for",
                 "no", "been", "why", "get", "what", "just", "has", "have", "how", "other", "had", "so", "when", "us", "your", "are", "if", "with", "at", "by", "from", "up", "about", "into", "over", "after", "was", "can", "do", "new", "does", ]
# it cleans the words


def count_comment(final_comment_list):
    for comment_word in final_comment_list:
        if comment_word not in neutral_words:
            if comment_word.__len__() not in [2, 1]:
                if dictionay.get(comment_word):
                    dictionay[comment_word] = dictionay[comment_word]+1
                else:
                    dictionay[comment_word] = 1


# slice_comments(comment_list)
