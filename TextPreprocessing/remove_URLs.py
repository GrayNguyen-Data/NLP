import re

# re = Regular Expression module nhằm tìm kiếm- so khớp - thay thế chuỗi theo mẫu
# (r'https?://\S+|www\.\S+') : Regex pattern để tìm ỦRL bắt đầu bằng https

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)