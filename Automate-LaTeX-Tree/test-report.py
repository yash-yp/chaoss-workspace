import pathlib
import os
import shutil
import pypandoc
import re


def check_subarray(subarr, arr):
    for element in subarr:
        if element not in arr:
            return False
    return True

def copy_file(source_filepath, dest_path):
    if os.path.isfile(dest_path):
        print(f"File with same name already exists at destination: {source_filepath}")
    else:
        print(f"Copying: {source_filepath}")
        shutil.copy(source_filepath, dest_path)
        print(f"Copied Successfully")

def convert_md2tex(md_filename, latex_filename):
    print(f"Converting {md_filename} file to LaTeX")
    # using 'gfm' results in page overflow of tables hence 'markdown_github'  used
    output = pypandoc.convert_file(md_filename, 'latex', outputfile=latex_filename, extra_args=['-f', 'markdown_github'])

    assert output == ""
    print(f"Created successfully: {latex_filename}")

def convert_tex2pdf(tex_filename, pdf_filename):
    print(f"Converting {tex_filename} file to PDF")

    output = pypandoc.convert_file(tex_filename, 'pdf', outputfile=pdf_filename, extra_args=['-f', 'latex',
                                                                                            '--pdf-engine=xelatex',
                                                                                             '-H', 'header.tex',
                                                                                             '--highlight-style', 'zenburn',
                                                                                             '-V', 'geometry:margin=0.8in',
                                                                                             '-V', 'monofont:DejaVuSansMono.ttf',
                                                                                             '-V', 'mathfont:texgyredejavu-math.otf',
                                                                                             '-V', 'geometry:a4paper',
                                                                                             '-V', 'colorlinks=true',
                                                                                             '-V', 'linkcolour:blue',
                                                                                             '-V', 'fontsize=12pt',
                                                                                             '--toc', '--toc-depth= 1'
                                                                                            ])
    assert output == ""
    print(f"Conversion process successful: {pdf_filename}")

def delete_files(file_path_arr):
    for file_path in file_path_arr:
        try:
            if os.path.isfile(file_path):
                print(f"Deleting: {file_path}")
                os.remove(file_path)
                print(f"Deleted Successfully")
        except:
            print(f"Unable to delete {file_path}")

def delete_folder(folder_path):
    try:
        if os.path.isdir(folder_path):
            print(f"Deleting folder: {folder_path}")
            shutil.rmtree("images")
            print("Deleted Successfully")
    except:
        print(f"Unable to delete folder: {folder_path}")


if __name__=="__main__":

    script_dir_path = pathlib.Path(__file__).parent.absolute()
    common_images_folder_path = os.path.join(script_dir_path, "images")
    repo_name = "wg-common"
    blacklisted_files_list = ["README.md"]
    root = os.path.join(script_dir_path, repo_name, "focus-areas")
    final_report_pdf = "test-release.pdf"
    converted_tex_files = []

    # code to copy all the images from each focus-area to a common images folder
    if not os.path.isdir("images"):
        os.mkdir("images")

    for folder, sub_folders, files in os.walk(root):
        for file in files:
            if folder.endswith("images"):
                source_filepath = os.path.join(script_dir_path, folder, file)
                dest_path = os.path.join(script_dir_path, "images", file)
                copy_file(source_filepath,dest_path)

    # copy required metric files and convert them to latex
    for folder, sub_folders, files in os.walk(root):

        # check for images folder or if all elements of files are blacklisted
        if folder.endswith("images") or check_subarray(files, blacklisted_files_list):
            continue
        copied_metric_md_list = []
        for file in files:
            if file not in blacklisted_files_list:
                source_filepath = os.path.join(script_dir_path, folder, file)
                dest_path = os.path.join(script_dir_path, file)
                copy_file(source_filepath, dest_path)
                copied_metric_md_list.append(file)
                print(os.path.relpath(folder))
                print(os.path.split(folder)[1])
                tex_filename = re.sub(".md",".tex",file)
                convert_md2tex(file,tex_filename)
                converted_tex_files.append(tex_filename)

        # once converted to latex, individual metric files are no longer required
        delete_files(copied_metric_md_list)

    # create required report
    repo_tex_filename = repo_name+".tex"
    convert_tex2pdf(repo_tex_filename,final_report_pdf)

    # code to remove inessential files
    delete_files(converted_tex_files)
    delete_folder("images")