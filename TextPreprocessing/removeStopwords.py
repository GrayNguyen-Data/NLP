# Stopwords: Là những từ thường xuyên xuất hiện trong văn bản nhưng không mang nhiều ý nghĩa quan trọng

# Đối với tiếng việt: Là các từ như "và", "là", "của", "trong", "đang", "một",...
# Đối với tiếng anh: Là các từ như "and", "is", "the", "in", "a",...

#  Sử dụng thư viện nltk = Natural Language Tookit
# Lưu ý: Stopwords không hỗ trợ ngôn ngữ tiếng việt, thay vào đó ta có thể tạo 1 danh sách các stopwords riêng cho tiếng việt
# Việc mà mình remove stopwords nhằm mục đích là để giúp mô hình tập trung vào các keywords quan trọng trong văn bản hơn

# Thuật ngữ: TF-IDF (Term Frequency - Inverse Document Frequency) là phương pháp biểu diễn text thành số học,  TF: Tần xuất từ, IDF: Độ hiếm từ trong tài liệu

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words("english"))

def remove_stopwords_v1(text):
    text = text.split()
    texts = []
    for word in text:
        if word not in STOPWORDS:
            texts.append(word)
    return ' '.join(texts)

# clean code 1 chút nào bro
def remove_stopwords_v2(text):
    return " ".join([word for word in text.split() if word not in STOPWORDS])
if __name__ == "__main__":
    print(remove_stopwords_v1("This is a sample sentence to demonstrate the removal of stopwords."))
    print(remove_stopwords_v2("This is a sample sentence to demonstrate the removal of stopwords."))
    