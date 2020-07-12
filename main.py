import os
import requests
import argparse
import base64
from pathlib import Path

def main(url: str, dest: str):
    # Change to destination directory
    prev_dir = os.curdir

    # Enter the destination path
    if not os.path.exists(dest):
        Path(dest).mkdir(parents=True, exist_ok=True)
    os.chdir(dest)

    def pull(pull_url: str, current_path: str = ''):
        res = requests.get(pull_url).json()
        if 'content' in res:
            content = base64.b64decode(res['content']).decode('utf-8')

            # Write to file
            parent_dir = os.path.dirname(current_path)
            Path(parent_dir).mkdir(parents=True, exist_ok=True)
            with open(current_path, 'w') as file:
                file.write(content)
        elif 'tree' in res:
            # Get all tree nodes
            for obj in res['tree']:
                pull(obj['url'], os.path.join(current_path, obj['path']))

    # Pull files recursively
    pull(url)

    # Go back to original directory
    os.chdir(prev_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download all GitHub tree files recursively.')
    parser.add_argument('url', type=str, help='URL of the tree in the GitHub API (i.e. https://api.github.com/repos/<username>/<repo>/git/trees/<tree_sha>')
    parser.add_argument('dest', default='.', nargs='?', help='destination folder')

    args = parser.parse_args()
    main(args.url, args.dest)