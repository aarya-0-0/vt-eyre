import tkinter as tk
from tkinter import filedialog, scrolledtext
from vt_eyre import scanner
import io
import sys

# Function to redirect print output to the text widget
class TextRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, s):
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, s)
        self.text_widget.see(tk.END)
        self.text_widget.configure(state='disabled')

    def flush(self):
        pass  # Needed for sys.stdout compatibility

# Scan URL
def scan_url():
    url = url_entry.get()
    if url:
        result_text.configure(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.configure(state='disabled')
        # Redirect stdout to GUI
        sys.stdout = TextRedirector(result_text)
        try:
            scanner.scan_url(url)
        except Exception as e:
            print(f"❌ Error: {e}")
        sys.stdout = sys.__stdout__  # Reset to default

# Scan File
def scan_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        result_text.configure(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.configure(state='disabled')
        # Redirect stdout to GUI
        sys.stdout = TextRedirector(result_text)
        try:
            scanner.scan_file(file_path)
        except Exception as e:
            print(f"❌ Error: {e}")
        sys.stdout = sys.__stdout__  # Reset to default

# GUI setup
root = tk.Tk()
root.title("VT-Eyre GUI Scanner")
root.geometry("700x500")

# URL input
tk.Label(root, text="Enter URL to scan:").pack(pady=5)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)
tk.Button(root, text="Scan URL", command=scan_url).pack(pady=5)

# File scan button
tk.Button(root, text="Scan File", command=scan_file).pack(pady=5)

# Results area
result_text = scrolledtext.ScrolledText(root, width=80, height=25, state='disabled')
result_text.pack(pady=10)

root.mainloop()
