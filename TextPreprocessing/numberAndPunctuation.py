
# Xóa bỏ số và dấu câu khỏi văn bản hoặc xem dấu câu hay số là một token riêng biệt

import string

PUNCTUATION_TO_REMOVE = str(string.digits + string.punctuation)

# Xóa cả số và dấu câu
def remove_numbers_and_punctuation(text):
    for token in PUNCTUATION_TO_REMOVE:
        text = text.replace(token, '')
    return text



# Xem số và dấu câu là token riêng biệt

PUNCTUATION_TO_REMOVE = str(string.punctuation)
def convert_punc(text):
    for token in PUNCTUATION_TO_REMOVE:
        text = text.replace(token, ' ' + token + ' ')
    return text

if __name__ == "__main__":
    print(convert_punc("Hello, world! It's 2024."))  
    print(remove_numbers_and_punctuation("Hello, world! It's 2024."))  