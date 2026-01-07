# Sử dụng thư viện autocorect để sửa lỗi chính tả trong văn bản

from autocorrect import spell
def correct_spelling(text):
    text = text.split()
    corrected_texts = []
    for word in text:
        corrected_texts.append(spell(word))
    return ' '.join(corrected_texts)
if __name__ == "__main__":
    print(correct_spelling("Ths is a smaple sentnce with sme speling erors."))