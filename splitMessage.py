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
                    elif brace_count < 0:
                        break
            parts.append(content[start_delimiter_pos:end_delimiter_pos + 1])
            start = end_delimiter_pos + 1
    return parts

def save_strings_with_start(parts, start_string):
    result_strings = []
    for part in parts:
        if part.startswith(start_string):
            if start_string == '{3:':
                # Nếu bắt đầu bằng {3:, xử lý đặc biệt nếu sau đó là {
                brace_pos = part.find('{', len(start_string))
                if brace_pos != -1:
                    end_index = part.find('}', brace_pos)
                    if end_index != -1:
                        result_strings.append(part[brace_pos:end_index + 1])
            elif start_string == '{4:':
                brace_pos = part.find('{', len(start_string))
                if brace_pos != -1:
                    end_index = part.find('}', brace_pos)
                    if end_index != -1:
                        # Kiểm tra xem chuỗi kết thúc bằng '-}'
                        if part.endswith('-}'):
                            # Cắt đến trước '-}'
                            result_strings.append(part[brace_pos:end_index - 2])
                        else:
                            # Cắt như bình thường
                            result_strings.append(part[brace_pos:end_index + 1])
            else:
                start_index = part.find(start_string) + len(start_string)
                end_index = part.find('}')
                if end_index != -1:
                    result_strings.append(part[start_index:end_index])
    return result_strings

file_path = 'MTMessage.txt'
parts = split_by_delimiter(file_path)

# Lưu các chuỗi bắt đầu bằng '1'
result_strings = save_strings_with_start(parts, '{1:')
print("Block 1")
for string in result_strings:
    print(string)

# Lưu các chuỗi bắt đầu bằng '2'
result_strings = save_strings_with_start(parts, '{2:')
print("Block 2")
for string in result_strings:
    print(string)

# Lưu các chuỗi bắt đầu bằng '3:'
result_strings = save_strings_with_start(parts, '{3:')
print("Block 3")
for string in result_strings:
    print(string)

# Lưu các chuỗi bắt đầu bằng '4:'
result_strings = save_strings_with_start(parts, '{4:')
print("Block 4")
for string in result_strings:
    print(string)
