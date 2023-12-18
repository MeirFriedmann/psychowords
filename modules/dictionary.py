import PyPDF2
def extract_words_from_srt(srt_file_path):
    words = []
    with open(srt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            # Ignore empty lines and lines with timestamps
            if line.strip() and not line.startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
                # Split the line into words
                line_words = line.split()

                # Add words to the list
                words.extend(line_words)

    return words

# Example usage
srt_file_path = '/home/meir/Projects/psychowords/assets/subs.srt'
subtitle_words = extract_words_from_srt(srt_file_path)



def clean_non_english(input_string):
    english_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')
    cleaned_string = ''.join(char for char in input_string if char in english_chars)
    return cleaned_string


def extract_lines_from_pdf(pdf_path):
    lines = []
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Iterate through each page
        for page_num in range(16):
            # Get the page
            page = pdf_reader.pages[page_num]

            # Extract text from the page
            page_text = page.extract_text()

            # Split the text into lines and add to the list
            lines.extend(page_text.split('\n'))

    return lines

# Example usage
pdf_path = "/home/meir/Projects/psychowords/assets/ENG_DIC_CAMPUS.pdf"
lines = extract_lines_from_pdf(pdf_path)
lines = [line for line in lines if len(line) > 1]
words = []
for line in lines:
    words.append(clean_non_english(line)[:-3])

new = set()
for word in subtitle_words:
    if word in words:
        new.add(word)

print(new)

with open(srt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            # Ignore empty lines and lines with timestamps
            if line.strip() and not line.startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
                # Split the line into words
                for n in new:
                    if n in line.split(): 
                        print(line, "")
                        print(n)

