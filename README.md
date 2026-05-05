🔍 File Type Analyzer (DFIR Tool)

 📌 Overview
A CLI-based Digital Forensics (DFIR) tool that detects file type spoofing by analyzing **magic bytes (file signatures)** instead of relying on file extensions.

 🚀 Features
- Detects real file type from binary signatures
- Identifies spoofed files (e.g., `.exe` disguised as `.jpg`)
- Scans single files or entire directories
- Generates structured JSON report
- Simple CLI interface

🧪 Example
[⚠] samples/fake.jpg → exe
[✔] samples/IMP.png → png

 🛠️ Usage
```bash
py analyzer.py <file_or_folder>
