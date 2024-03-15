def split_by_delimiter(file_path, delimiter='{'):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        parts = []
        start = 0
        brace_count = 0  # Biến đếm số lượng dấu '{'
        while True:
            start_delimiter_pos = content.find(delimiter, start)
            if start_delimiter_pos == -1:
                break
            end_delimiter_pos = start_delimiter_pos  # Mặc định là bắt đầu từ vị trí của dấu '{'
            brace_count = 1  # Bắt đầu đếm từ dấu '{' đầu tiên
            for i in range(start_delimiter_pos + 1, len(content)):
                if content[i] == '{':
                    brace_count += 1
                elif content[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:  # Nếu số lượng dấu '{' và '}' bằng nhau
                        end_delimiter_pos = i
                        break
                if brace_count < 0:  # Trong trường hợp không có dấu '}' phù hợp sau dấu '{' đầu tiên
                    break
            parts.append(content[start_delimiter_pos:end_delimiter_pos + 1])
            start = end_delimiter_pos + 1
    return parts

file_path = 'MTMessage.txt'
parts = split_by_delimiter(file_path)
for part in parts:
    print(part)
