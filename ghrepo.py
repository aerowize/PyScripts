import os
import sys


project_name = sys.argv[1]
commit_message = sys.argv[2]


def validate(input):
    if len(input) < 3:
        print('[!] Requires 2 arguments!!!')
        sys.exit(1)


def run_commands(project, cmds):
    os.chdir(project)
    try:
        for c in cmds:
            os.system(c)
    except:
        print("Git Error")
        sys.exit(1)


first_commit = f'echo "# {project_name}" >> README.md && git init && git add README.md && git commit -m "{commit_message}"'
branch_remote = f'git branch -M main && git remote add origin https://github.com/aerowize/{project_name}.git'
gh_push = 'git push -u origin main'

commands = [first_commit, branch_remote, gh_push]


if __name__ == "__main__":
    validate(sys.argv)
    run_commands(project_name, commands)
