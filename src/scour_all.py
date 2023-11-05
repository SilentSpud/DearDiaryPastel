import os
import subprocess

scour_args = ['--quiet', '--remove-titles', '--create-groups', '--remove-descriptions', '--remove-descriptive-elements', '--remove-metadata', '--enable-comment-stripping', '--indent=space', '--nindent=2', '--strip-xml-space']

def scour_all():
    # Traverse all subdirectories under the svg folder
    for root, dirs, files in os.walk('svg'):
        for file in files:
            if file.endswith('.svg'):
                # Run scour on the file 3 times and replace the original file with the scour output
                input_file = os.path.join(root, file)
                output_file1 = os.path.join(root, os.path.splitext(file)[0] + ".svg.1.tmp")
                output_file2 = os.path.join(root, os.path.splitext(file)[0] + ".svg.2.tmp")
                output_file3 = os.path.join(root, os.path.splitext(file)[0] + ".svg.3.tmp")
                print('Scouring ' + input_file + '...')
                subprocess.run(['scour', input_file, output_file1] + scour_args)
                subprocess.run(['scour', output_file1, output_file2] + scour_args)
                subprocess.run(['scour', output_file2, output_file3] + scour_args)
                os.remove(output_file1)
                os.remove(output_file2)
                os.replace(output_file3, input_file)
            