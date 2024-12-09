import heapq

from collections import Counter
import math


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def make_frequency_dict(self, text):
        return Counter(text)

    def build_heap(self, frequency):
        for key, freq in frequency.items():
            heapq.heappush(self.heap, (freq, key))

    def build_tree(self):
        while len(self.heap) > 1:
            freq1, char1 = heapq.heappop(self.heap)
            freq2, char2 = heapq.heappop(self.heap)
            heapq.heappush(self.heap, (freq1 + freq2, (char1, char2)))

    def build_codes(self, node, current_code=""):
        if isinstance(node, str):
            self.codes[node] = current_code
            self.reverse_mapping[current_code] = node
            return

        left, right = node
        self.build_codes(left, current_code + "0")
        self.build_codes(right, current_code + "1")

    def huffman_encoding(self, text):
        frequency = self.make_frequency_dict(text)
        self.build_heap(frequency)
        self.build_tree()
        root = heapq.heappop(self.heap)[1]
        self.build_codes(root)
        return "".join(self.codes[char] for char in text)

    def huffman_decoding(self, encoded_text):
        current_code = ""
        decoded_text = []
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text.append(self.reverse_mapping[current_code])
                current_code = ""
        return "".join(decoded_text)

    def calculate_entropy(self, text):
        frequency = self.make_frequency_dict(text)
        total_chars = len(text)
        entropy = -sum(
            (freq / total_chars) * math.log2(freq / total_chars)
            for freq in frequency.values()
        )
        return entropy
