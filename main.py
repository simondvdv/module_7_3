class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for i in files:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                list_words = []
                for line in file:
                    list_words += punctuation_break(line).lower().split()
                all_words[i] = list_words
        return all_words

    def find(self, word):
        finded_word = {}
        for key, values in WordsFinder.get_all_words(self).items():
            try:
                finded_word[key] = values.index(word.lower()) + 1
                return finded_word
            except ValueError:
                continue
        return 'Такого слова в файлах нет'

    def count(self, word):
        finded_word = {}
        for key, values in WordsFinder.get_all_words(self).items():
            if values.count(word.lower()) != 0:
                finded_word[key] = values.count(word.lower())
        if len(finded_word) != 0:
            return finded_word
        else:
            return 'Такого слова в файлах нет'


def punctuation_break(string):
    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
    for i in punctuation:
        string = string.replace(i, '')
    return string


finder1 = WordsFinder('test_file.txt', 'Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
print(finder1.find('TEXT')) # 3 слово по счёту
print(finder1.count('teXT')) # 4 слова teXT в тексте всего
