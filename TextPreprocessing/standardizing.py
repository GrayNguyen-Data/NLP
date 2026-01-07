# Chuẩn hóa các từ viết tắt thành dạng đầy đủ
# Ví dụ: DM -> Direct message, info -> information

dict_lock = {
    'DM': 'Direct Message',
    'info': 'Information'
}

def standardize_text(text):
    for k, v in dict_lock.items():
        text = text.replace(k, v)
    return text
print(standardize_text("Please send me a DM for more info."))  