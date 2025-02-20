import os
import subprocess

def download_dataset():
    """Downloads the earthquake dataset from GitHub."""
    repo_url = "https://github.com/SofiaAngelico/ai-learning.git/" 
    dataset_dir = "ai-learning"  # Name of the directory to store the dataset

    if not os.path.exists(dataset_dir):
        # Clone the repository if it doesn't exist
        subprocess.run(["git", "clone", repo_url], check=True)
    else:
        print("Dataset directory already exists. Skipping download.")

    print("Dataset downloaded successfully!")

if __name__ == "__main__":
    download_dataset()
