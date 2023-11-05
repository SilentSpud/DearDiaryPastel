import os
import subprocess
import json

def patch_swfs():
    # paths.json maps svg folders to their respective swf files
    with open('paths.json') as f:
        data = json.load(f)

    for svg_dir, swf_path in data.items():
        out_path = os.path.join('out', os.path.normpath(os.path.split(swf_path)[0]))
        out_file = os.path.join(out_path, os.path.split(swf_path)[1])
        swf_path = os.path.join('base', os.path.normpath(swf_path))
        svg_dir = os.path.join('svg', os.path.normpath(svg_dir))
        # Create output directory matching swf path if it doesn't exist
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        
        print('Patching ' + swf_path + ' to ' + out_file)
        subprocess.run(['java', '-jar', os.path.join('jpexs', 'ffdec.jar'), '-cli', '-importShapes', swf_path, out_file, svg_dir])