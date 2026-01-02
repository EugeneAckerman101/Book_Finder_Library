import os
import shutil


def search_pdfs(directory, keyword):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf') and keyword.lower() in file.lower():
                result.append(os.path.join(root, file))
    return result

# Change 'your_directory_path' to the path of your folder with the PDFs
directory_path = r"C:\Users\Eugene\Documents\4_Private_New\E-Books\_OceanofPDF"
search_keyword = 'AI'

# Define the output directory on your Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_dir = os.path.join(desktop_path, "book_search")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

#=== MAIN ===


matching_pdfs = search_pdfs(directory_path, search_keyword)
print(f"PDF files containing '{search_keyword}' in filename:")
if not matching_pdfs:
    print("No matching files found")
else:
    for pdf in matching_pdfs:
        print(pdf)
        try:
            filename = os.path.basename(pdf)
            destination = os.path.join(output_dir, filename)
            shutil.copy2(pdf, destination) # preserves metadata
            print(f"→ Copied to {destination}")
        except Exception as e:
            print(f"× Error copying '{pdf}': {e}")
