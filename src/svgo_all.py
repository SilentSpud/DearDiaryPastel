import subprocess
import os

svgo_args = []

def svgo_all():
    # Traverse all subdirectories under the svg folder
    for root, dirs, files in os.walk('svg'):
        for file in files:
            if file.endswith('.svg'):
                # Run svgo on the file
                input_file = os.path.join(root, file)
                subprocess.run(['svgo', input_file, '-o', input_file] + svgo_args)