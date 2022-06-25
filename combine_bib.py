import os


def get_dirs_and_files(first_dir):
    '''Returns dict, where key is directory full path and values is the list
    of files that are to be processed'''
    content = {}

    for root, _, files in os.walk(first_dir):
        content[root] = files

    return content


def process_file(input_file, biblios):
    with open(input_file, encoding='utf8') as f:
        lines_list = list(f.readlines())
        start = lines_list.index('```\n')
        lines_list = lines_list[start + 1:]
        end = lines_list.index('```\n')
        lines_list = lines_list[:end]

    biblios.append(lines_list)


def write_bib_file(path, biblios):
    with open(path, 'w', encoding='utf8') as fw:
        for bib in biblios:
            fw.writelines(bib)
            fw.write('\n')


def main():
    root = os.path.join(os.path.curdir, 'obsidian_vault_litobzor')
    file_path = '../my_thesis_in_latex/biblio/external.bib'
    dirs = get_dirs_and_files(root)
    dirs.pop('.\\obsidian_vault_litobzor')
    dirs.pop('.\\obsidian_vault_litobzor\\.obsidian')
    dirs.pop('.\\obsidian_vault_litobzor\\.obsidian\\themes')
    dirs.pop('.\\obsidian_vault_litobzor\\6. IS eval using NDT')
    dirs.pop('.\\obsidian_vault_litobzor\\7. Plastic deformations')
    dirs.pop('.\\obsidian_vault_litobzor\\8. Unsorted')
    dirs.pop('.\\obsidian_vault_litobzor\\10. FYI')

    biblios = []

    for directory, files in dirs.items():
        for file in files:
            input_file = os.path.join(directory, file)
            process_file(input_file, biblios)

    write_bib_file(file_path, biblios)


if __name__ == '__main__':
    main()
