import os
import subprocess
import math

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running: {cmd}\nOutput: {result.stderr}")
    return result

def main():
    print("Initializing Git Repository...")
    run_cmd("git init")
    
    # exclude .git folder
    all_files = []
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
        for file in files:
            all_files.append(os.path.normpath(os.path.join(root, file)))
            
    total_files = len(all_files)
    target_commits = 50
    print(f"Found {total_files} files to commit into {target_commits} commits.")
    
    # Calculate how many extra commits we need if files < 50
    if total_files < target_commits:
        print("Not enough files to make 50 distinct file commits. Falling back to 1 file per commit and empty commits.")
    
    files_per_commit = max(1, total_files // target_commits)
    
    commit_count = 0
    file_index = 0
    
    # Group files into commits
    while file_index < total_files:
        # Determine files for this commit
        chunk_size = files_per_commit
        if commit_count >= target_commits - 1:
            # Last commit takes the remainder
            chunk_size = total_files - file_index
        elif commit_count < (total_files % target_commits):
            # Distribute remainder evenly
            chunk_size = files_per_commit + 1

        files_chunk = all_files[file_index:file_index + chunk_size]
        
        for file in files_chunk:
            run_cmd(f'git add "{file}"')
            
        file_names_str = ", ".join([os.path.basename(f) for f in files_chunk])
        commit_msg = f"Add {file_names_str}"
        run_cmd(f'git commit -m "{commit_msg[:50]}..."')
        
        commit_count += 1
        file_index += chunk_size
    
    # If we still haven't reached 50, pad with empty commits
    while commit_count < target_commits:
        run_cmd('git commit --allow-empty -m "Incremental update to project structure"')
        commit_count += 1

    print(f"Successfully generated {commit_count} commits.")

if __name__ == "__main__":
    main()
