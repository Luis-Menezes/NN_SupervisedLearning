import kagglehub
import pandas as pd

# Download latest version
def download_and_load_dataset():
    path = kagglehub.dataset_download("zadafiyabhrami/global-crocodile-species-dataset") + "/crocodile_dataset.csv"
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = download_and_load_dataset()
    print("Dataset preview:\n", df.info())
    # print("Files in dataset:", kagglehub.list_files(path))