# Xử lý các emoji và emoticon trong văn bản
# Emoji: Biểu tượng cảm xúc dạng hình ảnh, ví dụ: 😊, 😢
# Emoticon: Biểu tượng cảm xúc dạng ký tự, ví dụ: :-), :-(

import emot
emot_obj = emot.emot()
def convert_emoji(text):
    for emoji, mean in zip(emot_obj.emoji(text)['value'], emot_obj.emoji(text)['mean']):
        text =text.replace(emoji, mean.replace(":", ""))
    return text

def convert_emoticon(text):
    dict_emotions = dict(zip(emot_obj.emoticons(text)['value'], emot_obj.emoticons(text)['mean']))
    sorted_emotions = sorted(dict_emotions.items(),key = lambda kv: len(kv[0]), reverse=True)
    for emoticon, mean in sorted_emotions:
        text = text.replace(emoticon, mean)
        print(text)
    return text
if __name__ == "__main__":
    sample_text = "I am so happy today! 😊 But sometimes I feel sad. 😢"
    print(convert_emoji(sample_text))
    sample_text2 = "Hello there! :-) How are you? :-("
    print(convert_emoticon(sample_text2))
