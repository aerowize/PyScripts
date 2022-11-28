#!/usr/bin/env python3

import sys
import os


def create_structure(name):
    # Create the root folder based upon the
    # users provided name and then create the
    # folders inside.
    folders = ['scripts', 'styles', 'images']
    os.mkdir(name)
    os.chdir(name)
    for f in folders:
        os.mkdir(f)

 # HTML Boilerplate
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./styles/style.css">
</head>
<body>
    <script src="./scripts/app.js"></script>
</body>
</html>
"""

# CSS Boilerplate
css = """
* {
    margin: 0;
    padding: 0;
    border: 0;
    box-sizing: border-box;
}

body {
    background-color: darkslategray;
}
"""

# Create the file and write the text to it


def create_file(file, text):
    with open(file, 'w') as f:
        f.write(text)
        f.close()


if __name__ == "__main__":
    project_name = sys.argv[1]  # Name of the root directory from user input

    create_structure(project_name)
    create_file('index.html', html)
    create_file('style.css', css)
    os.system('touch app.js')  # Create the js file, Has no boilerplate
    print(f"[+] {project_name} created!")
