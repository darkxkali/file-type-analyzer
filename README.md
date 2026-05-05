🔍 File Type Analyzer (DFIR Tool)



📌 Description

This is a CLI-based digital forensics tool that detects file type spoofing using magic bytes instead of file extensions.



🚀 Features

\- Detects real file type from binary signature

\- Identifies spoofed files (e.g., .exe renamed to .jpg)

\- Scans entire directories

\- Generates JSON report



🧪 Example Output



\[⚠] samples/fake.jpg → exe  

\[✔] samples/IMP.png → png  



🛠️ Usage



py analyzer.py <file/folder>



📂 Output

\- Console results

\- report.json file



🧠 DFIR Use Case

Attackers disguise malicious files by changing extensions. This tool helps detect such threats.

