
import re
# re = Regular Expression module nhằm tìm kiếm- so khớp - thay thế chuỗi theo mẫu
# (<.*?>) : Regex pattern để tìm thẻ HTML
def remove_html(text):
    html_pattern =  re.compile('<.*?>')
    return html_pattern.sub(r'', text)