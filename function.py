import requests

def get_repocomit(user_id):
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    repos_response = requests.get(repos_url)
    
    if repos_response.status_code != 200:
        raise Exception(f"Failed to fetch repositories for user {user_id}: {repos_response.status_code}")
    
    repos = repos_response.json()
    repo_commits = []
    
    for repo in repos:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)
        
        # Handle 409 (empty repo)
        if commits_response.status_code == 409:
            print(f"Repo {repo_name} has no commits or is in a conflicted state.")
            repo_commits.append(f"Repo: {repo_name} Number of commits: 0")
            continue
        
        if commits_response.status_code != 200:
            raise Exception(f"Failed to fetch commits for repo {repo_name}: {commits_response.status_code}")
        
        commits = commits_response.json()
        commit_count = len(commits)
        repo_commits.append(f"Repo: {repo_name} Number of commits: {commit_count}")
    
    return repo_commits

if __name__ == "__main__":
    user_id = "ashmi2001"
    repos_and_commits = get_repocomit(user_id)
    for repo in repos_and_commits:
        print(repo)
