import re
from collections import Counter
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file: str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)

        print('Pages: ', len(reader.pages))
        print('-' * 10) # Divider

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text

def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())

        all_words += [word for word in split_text if word]
        return Counter(all_words)

def main():
    extracted_text: list[str] = extract_text_from_pdf('sample.pdf')
    counter: Counter = count_words(text_list = extracted_text)

    for page in extracted_text:
        print(page)

    for word, count in counter.most_common(3):
        print(f'{word:10}: {count} times')

    chars = Counter()
    for char in extracted_text:
        for x in char:
            chars[x] += 1
    print(f'Total characters: {chars.total()}')

if __name__ == '__main__':
    main()
