import os

def extract_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text_from_directory(directory_path):
    combined_text = ""
    for filename in os.listdir(directory_path):
        if filename.endswith('.m3u') or filename.endswith('.m3u8'):
            file_path = os.path.join(directory_path, filename)
            extracted_text = extract_text_from_file(file_path)
            combined_text += extracted_text + "\n"
    return combined_text

def save_combined_text(combined_text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(combined_text)

if __name__ == "__main__":
    directory_path = input("Enter the directory path containing .m3u and .m3u8 files: ")
    output_file = input("Enter the output .m3u file name: ")
    
    combined_text = extract_text_from_directory(directory_path)
    save_combined_text(combined_text, output_file)
    
    print(f"Combined text has been saved to {output_file}")