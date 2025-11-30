import os

def list_files(folder_path):
    try:
        return os.listdir(folder_path)
    except Exception as e:
        return f"Error: {e}"

def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def main():
    print("📄 DocuMind – Simple Document Reader")
    folder = input("Enter folder path: ")

    files = list_files(folder)
    print("\nFiles found:", files)

    if isinstance(files, list):
        file_name = input("\nEnter file name to read: ")
        file_path = os.path.join(folder, file_name)
        content = read_file(file_path)

        print("\n--- File Content ---\n")
        print(content)

if __name__ == "__main__":
    main()

