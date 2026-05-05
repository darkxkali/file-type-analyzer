import sys
import os
import json

FILE_SIGNATURES = {
    "jpg": b"\xFF\xD8\xFF",
    "png": b"\x89\x50\x4E\x47",
    "pdf": b"\x25\x50\x44\x46",
    "exe": b"\x4D\x5A",
    "zip": b"\x50\x4B\x03\x04"
}

def detect_type(header):
    for file_type, sig in FILE_SIGNATURES.items():
        if header.startswith(sig):
            return file_type
    return "unknown"

def analyze_file(file_path):
    try:
        with open(file_path, "rb") as f:
            header = f.read(8)
    except:
        return None

    detected = detect_type(header)

    ext = file_path.split(".")[-1].lower() if "." in file_path else "none"

    status = "OK" if detected == ext else "suspicious"

    return {
        "file": file_path,
        "extension": ext,
        "detected": detected,
        "status": status
    }

def scan_folder(folder):
    results = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            result = analyze_file(path)
            if result:
                results.append(result)

    return results

def save_report(results):
    with open("report.json", "w") as f:
        json.dump(results, f, indent=4)

    print("\n[+] Report saved as report.json")

def main():
    if len(sys.argv) != 2:
        print("Usage: py analyzer.py <file/folder>")
        return

    target = sys.argv[1]

    if os.path.isfile(target):
        result = analyze_file(target)
        print(result)

    elif os.path.isdir(target):
        results = scan_folder(target)

        for r in results:
            status_icon = "⚠" if r["status"] == "suspicious" else "✔"
            print(f"[{status_icon}] {r['file']} → {r['detected']}")

        save_report(results)

    else:
        print("[ERROR] Invalid path")

if __name__ == "__main__":
    main()