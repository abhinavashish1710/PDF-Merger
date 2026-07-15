# 📄 PDF Merger

A simple and lightweight Python application that automatically merges multiple PDF files into a single PDF document using the **pypdf** library.

---

## ✨ Features

- Merge multiple PDF files into one
- Automatically detects all PDFs inside the `sample_pdfs` folder
- Preserves the original file order
- Automatically creates the output directory if it doesn't exist
- Lightweight and beginner-friendly
- Cross-platform (Windows, macOS, Linux)

---

## 📂 Project Structure

```
PDF-Merger/
│
├── sample_pdfs/
│   ├── sample1.pdf
│   ├── sample2.pdf
│   └── sample3.pdf
│
├── output/
│   └── merged.pdf
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/abhinavashish1710/PDF-Merger.git
```

### 2. Navigate to the project folder

```bash
cd PDF-Merger
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Place all PDF files inside the **sample_pdfs** folder.

2. Run the program:

```bash
python main.py
```

3. The merged PDF will be generated inside:

```
output/merged.pdf
```

---

## 💻 Example

### Input

```
sample_pdfs/
│
├── file1.pdf
├── file2.pdf
└── file3.pdf
```

### Console Output

```
Added: file1.pdf
Added: file2.pdf
Added: file3.pdf

Successfully merged 3 PDF(s).
Saved to: output/merged.pdf
```

### Output

```
output/
└── merged.pdf
```

---

## 🛠 Built With

- Python 3.12+
- pypdf 6.14.2
- os (Python Standard Library)

---

## 📦 Requirements

```
pypdf==6.14.2
```

---

## 🔮 Future Improvements

- GUI using Tkinter
- Drag-and-drop PDF support
- Merge selected pages only
- Rearrange PDF order before merging
- Password-protected PDF support
- PDF compression
- PDF splitting
- Display page count before merging

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Abhinav Ashish**

- GitHub: https://github.com/abhinavashish1710

---

⭐ If you found this project useful, consider giving it a star on GitHub!
