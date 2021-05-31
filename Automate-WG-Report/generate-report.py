import pathlib
import os
import shutil
import pypandoc
import re
from PyPDF2 import PdfFileMerger


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
        print(f"Copied Succesfully")

def merge_md(mdfile_list, merged_md_name):
    try:
        print(f"Merging markdown files")
        with open(merged_md_name, 'w') as outfile:
            for md_file in mdfile_list:
                with open(md_file) as infile:
                    print(f"Merging: {md_file}")
                    outfile.write(infile.read())
                outfile.write("\n")
        print(f"Markdown files merged successfully : {merged_md_name}")
    except:
        print(f"Error: Could not merge markdown files for {merged_md_name}")

def convert_md2pdf(md_filename, pdf_filename):
    print(f"Converting {md_filename} file to PDF")
    # using 'gfm' results in page overflow of tables hence 'markdown_github'  used
    output = pypandoc.convert_file(md_filename, 'pdf', outputfile=pdf_filename, extra_args=['-f', 'markdown_github',
                                                                                            '--pdf-engine=xelatex',
                                                                                            '-H', 'header.tex',
                                                                                            '--highlight-style','zenburn',
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
    print(f"Created successfully: {pdf_filename}")

def merge_pdf(pdf_list, pdf_filename):
    try:
        print("Merging PDF files")
        merger = PdfFileMerger()
        for pdf in pdf_list:
            print(f"Merging: {pdf}")
            merger.append(pdf)
        merger.write(pdf_filename)
        merger.close()
        print(f"PDF files merged successfully : {pdf_filename}")
    except:
        print("Error: Unable to merge PDF files")
        exit(1)

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
    focus_areas_mdlist = []
    final_report_pdf = "final-release.pdf"

    # code to copy all the images from each focus-area to a common images folder
    if not os.path.isdir("images"):
        os.mkdir("images")

    for folder, sub_folders, files in os.walk(root):
        for file in files:
            if folder.endswith("images"):
                source_filepath = os.path.join(script_dir_path, folder, file)
                dest_path = os.path.join(script_dir_path, "images", file)
                copy_file(source_filepath,dest_path)

    # code to copy metrics markdown files present in each focus area
    # and merge them alphabetically
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

        # At this point we will have the markdown files for a specific focus group in the common folder
        copied_metric_md_list.sort()
        regex_focus_area_name = r".*/"
        focus_area_name = re.sub(regex_focus_area_name, "", folder)
        focus_area_mdfile = focus_area_name + ".md"

        merge_md(copied_metric_md_list, focus_area_mdfile)
        focus_areas_mdlist.append(focus_area_mdfile)

        # once merged individual metric files are no longer required
        delete_files(copied_metric_md_list)

    # code to merge the generated for each focus area into a single md file
    focus_areas_mdlist.sort()
    repo_md_file = repo_name + ".md"

    merge_md(focus_areas_mdlist, repo_md_file)

    # since only one repository is being used the merged markdown files for that
    # repository will contain the all the required markdown elements that are to be converted
    inprocess_report_mdfile = repo_md_file
    inprocess_report_pdf = "inprocess-report.pdf"
    convert_md2pdf(inprocess_report_mdfile, inprocess_report_pdf)

    # code to remove individual markdown files for each focus-area
    delete_files(focus_areas_mdlist)

    # merge the generated pdf with the front matter to give final report
    report_pdf_elements = ["front-matter.pdf", inprocess_report_pdf]
    merge_pdf(report_pdf_elements, final_report_pdf)

    # delete other inessential files and images
    delete_files([repo_md_file, inprocess_report_pdf])
    delete_folder("images")
