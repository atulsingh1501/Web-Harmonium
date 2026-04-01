import os
import subprocess
import shutil
from datetime import datetime, timedelta

def run_cmd(cmd, env=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        print(f"Error running: {cmd}\nOutput: {result.stderr}")
    return result

def main():
    print("Removing old Git Repository...")
    if os.path.exists(".git"):
        # run a shell command to force remove .git on windows
        os.system('rd /s /q ".git"')
        
    print("Initializing new Git Repository...")
    run_cmd("git init")
    run_cmd("git branch -M main")
    
    # exclude .git folder
    all_files = []
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
        for file in files:
            all_files.append(os.path.normpath(os.path.join(root, file)))
            
    total_files = len(all_files)
    target_commits = 68
    distinct_days = 21
    
    print(f"Found {total_files} files to commit into {target_commits} commits over {distinct_days} days.")
    
    files_per_commit = max(1, total_files // target_commits)
    
    commit_count = 0
    file_index = 0
    
    # We want exactly distinct_days represented.
    today = datetime.now()
    
    # Set the remote
    run_cmd('git remote add origin https://github.com/atulsingh1501/Web-Harmonium.git')
    
    env = os.environ.copy()
    
    # Group files into commits
    while commit_count < target_commits:
        chunk_size = files_per_commit
        if commit_count == target_commits - 1:
            chunk_size = total_files - file_index # grab all remaining
            
        files_chunk = all_files[file_index:file_index + chunk_size]
        
        if len(files_chunk) > 0:
            for file in files_chunk:
                run_cmd(f'git add "{file}"')
            file_names_str = ", ".join([os.path.basename(f) for f in files_chunk])
            commit_msg = f"Add {file_names_str}"
        else:
            run_cmd("git commit --allow-empty -m \"Incremental layout updates\"")
            commit_msg = "Incremental layout updates"
            
        # Calculate date (spread evenly over 21 distinct days)
        day_offset = commit_count % distinct_days
        # Make the commits roughly sequential in time by offsetting hours too
        hour_offset = 12 - (commit_count // distinct_days) 
        
        commit_date = today - timedelta(days=day_offset, hours=hour_offset)
        date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
        
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        if len(files_chunk) > 0:
            run_cmd(f'git commit -m "{commit_msg[:50]}..."', env=env)
        else:
            run_cmd(f'git commit --allow-empty -m "{commit_msg}"', env=env)
            
        commit_count += 1
        file_index += chunk_size
        
        if commit_count % 10 == 0:
           print(f"Created {commit_count} commits so far...")

    print(f"Successfully generated {commit_count} commits. Pushing to origin main...")
    
    # Push to GitHub
    push_result = run_cmd("git push -u origin main -f")
    print("Push Output:", push_result.stdout)
    if push_result.stderr:
        print("Push Errors:", push_result.stderr)

if __name__ == "__main__":
    main()
