import pathlib
import os
import git

def clone_repo(repo_url, repo_name):
    if os.path.isdir(repo_name):
        print("Folder with same name already exists. Delete folder and then rerun this script")
    else:
        try:
            print(f"Cloning '{repo_name}' from {repo_url}")
            git.Repo.clone_from(repo_url, clone_to_path)
            print(f"Cloned Successfully")
        except:
            print(f"Error: Unable to clone {repo_url} repository")


if __name__=="__main__":
    repo_url = "https://github.com/chaoss/wg-common.git"
    repo_name = "wg-common"

    # absolute path of directory in which script is being run
    script_dir_path = pathlib.Path(__file__).parent.absolute()
    clone_to_path = os.path.join(script_dir_path, repo_name)

    clone_repo(repo_url,repo_name)




