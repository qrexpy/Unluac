import os
import subprocess
import shutil
import tkinter as tk
from tkinter import filedialog

def decrypt_lua_files(directory, base_output_dir):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.lua'):
                file_path = os.path.join(root, file)
                decrypted_file_path = os.path.join(base_output_dir, file.replace('.lua', '_decrypt.lua'))
                
                command = f'java -jar unluac.jar "{file_path}" > "{decrypted_file_path}"'
                subprocess.run(command, shell=True)
                
                final_file_path = decrypted_file_path.replace('_decrypt.lua', '.lua')
                os.rename(decrypted_file_path, final_file_path)
                
                shutil.move(final_file_path, file_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  
    directory = filedialog.askdirectory(title="Select Directory to Search for .lua Files")
    if directory:
        base_output_dir = os.path.dirname(__file__)
        decrypt_lua_files(directory, base_output_dir)