import os

import git
import pypandoc


def main():
    repo = git.Repo(os.getcwd())
    index = repo.index
    changed_files = [item.a_path for item in index.diff("HEAD") if item.a_path.endswith(".docx")]
    if not changed_files:
        print("No files to convert.")
        return

    print("Converting files to .md and adding to commit:")
    for file in changed_files:
        md_file = file.replace(".docx", ".md")
        pypandoc.convert_file(file, "html", outputfile=md_file)
        index.add([md_file])
        print(f"\t- {file} -> {md_file}")


if __name__ == "__main__":
    main()
