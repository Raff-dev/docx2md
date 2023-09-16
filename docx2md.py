import os

import git
import pypandoc


def main():
    repo = git.Repo(os.getcwd())
    index = repo.index
    changed_files = [item.a_path for item in index.diff("HEAD")]

    for file in changed_files:
        if file.endswith(".docx"):
            md_file = file.replace(".docx", ".md")
            pypandoc.convert_file(file, "markdown", outputfile=md_file)
            index.add([md_file])
            print(f"Converted {file} to {md_file} and added to commit.")


if __name__ == "__main__":
    main()
