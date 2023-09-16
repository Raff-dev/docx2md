import os

import git
import pypandoc


def main():
    repo = git.Repo(os.getcwd())
    index = repo.index
    changed_files = [item.a_path for item in index.diff("HEAD")]
    if not changed_files:
        print("No files to convert.")
        return

    print("Converting files to .md and adding to commit.")
    for file in changed_files:
        if file.endswith(".docx"):
            md_file = file.replace(".docx", ".md")
            pypandoc.convert_file(file, "html", outputfile=md_file)
            index.add([md_file])
            print(f"{file} - {md_file}")


if __name__ == "__main__":
    main()
