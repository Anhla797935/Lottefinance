import os
from git import Repo

# Thay đổi thông tin bên dưới
GITHUB_TOKEN = "github_pat_xxx"  # ← Dán token bạn đã tạo
USERNAME = "Anhla797935"       # ← Thay bằng GitHub username của bạn
REPO_NAME = "vaynhanh-lottefinance"

# Tạo URL GitHub
remote_url = f"https://{USERNAME}:{GITHUB_TOKEN}@github.com/{USERNAME}/{REPO_NAME}.git"

repo_dir = os.path.dirname(os.path.abspath(__file__))
repo = Repo.init(repo_dir)
repo.git.add(all=True)
repo.index.commit("Initial commit - upload website content")
origin = repo.create_remote('origin', remote_url)
origin.push(refspec='main:main')
print("✅ Code pushed to GitHub successfully.")
