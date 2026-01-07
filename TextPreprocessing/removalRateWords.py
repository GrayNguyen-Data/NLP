# Nhầm xóa đi các từ khan hiếm trong văn bản, mục tiêu là tập trung vào các keyword quan trọng.

Rate_WORDS = [
    "absolutely", "actually", "always", "basically", "certainly", "definitely"]
def remove_rate_words(text):
    text = text.split()
    texts = []
    for word in text:
        if word not in Rate_WORDS:
            texts.append(word)
    return ' '.join(texts)

