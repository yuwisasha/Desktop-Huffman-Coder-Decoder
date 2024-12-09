from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QLabel,
    QFileDialog,
)

from core.coder import HuffmanCoding


class HuffmanApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.huffman = HuffmanCoding()

    def init_ui(self):
        self.setWindowTitle("Huffman Coding")
        layout = QVBoxLayout()

        self.input_label = QLabel("Введите текст:")
        layout.addWidget(self.input_label)

        self.input_text = QLineEdit()
        layout.addWidget(self.input_text)

        self.load_button = QPushButton("Загрузить текст из файла")
        self.load_button.clicked.connect(self.load_file)
        layout.addWidget(self.load_button)

        self.encode_button = QPushButton("Закодировать текст")
        self.encode_button.clicked.connect(self.encode_text)
        layout.addWidget(self.encode_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.decode_button = QPushButton("Декодировать текст")
        self.decode_button.clicked.connect(self.decode_text)
        layout.addWidget(self.decode_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.information_label = QLabel("Энтропия (в битах):")
        layout.addWidget(self.information_label)

        self.information_text = QLabel("")
        layout.addWidget(self.information_text)

        self.setLayout(layout)

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Выберите текстовый файл", "", "Text Files (*.txt)"
        )
        if file_name:
            with open(file_name, "r", encoding="utf-8") as file:
                self.input_text.setText(file.read())

    def encode_text(self):
        text = self.input_text.text()
        if not text:
            self.result_text.setPlainText("Введите текст для кодирования.")
            return

        encoded_text = self.huffman.huffman_encoding(text)
        total_bits = self.huffman.calculate_entropy(text)

        self.result_label.setText("Результат кодирования:")
        self.result_text.setPlainText(encoded_text)
        self.information_text.setText(str(total_bits))

    def decode_text(self):
        text = self.input_text.text()
        if not text:
            self.result_text.setPlainText("Введите текст для декодирования.")
            return

        decoded_text = self.huffman.huffman_decoding(text)
        self.result_label.setText("Результат декодирования:")
        self.result_text.setPlainText(decoded_text)

        total_bits = self.huffman.calculate_entropy(decoded_text)
        self.information_text.setText(str(total_bits))
