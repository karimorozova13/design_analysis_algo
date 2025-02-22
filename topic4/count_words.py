from trie import Trie

class CountWords(Trie):

    def count_words_with_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for countWordsWithPrefix: prefix = {prefix} must be a string")

        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]

        return self._count_words(current)

    def _count_words(self, node):
        count = 1 if node.value is not None else 0
        for child in node.children.values():
            count += self._count_words(child)
        return count

# Ініціалізація Trie та вставка слів у словник
trie = CountWords()
words = ["apple", "application", "appetizer", "banana", "band", "banner", "ball", "bat", "battery"]

# Додаємо слова до Trie
for index, word in enumerate(words):
    trie.put(word, index)

# Підрахунок кількості слів, що починаються з префіксом "app"
count = trie.count_words_with_prefix("app")
print(f"Кількість слів із префіксом 'app': {count}")

def check_spelling(trie, word):
    if not isinstance(word, str) or not word:
        raise TypeError(f"Illegal argument for contains: key = {word} must be a non-empty string")
    return trie.get(word) is not None

# Приклади використання перевірки орфографії
words_to_check = ["apple", "app", "banner", "bat", "batman"]
for word in words_to_check:
    if check_spelling(trie, word):
        print(f"'{word}' написане правильно.")
    else:
        print(f"'{word}' не знайдено в словнику.")



