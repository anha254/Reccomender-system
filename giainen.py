import requests
import gzip
import shutil


# Tải tệp knn_model.pkl.gz từ GitHub (hoặc bạn có thể tải nó từ một URL nếu cần)
url = "https://github.com/anha254/Reccomender-system/raw/master/knn_model.pkl.gz"
r = requests.get(url)
with open("knn_model.pkl.gz", "wb") as f:
    f.write(r.content)

# Giải nén tệp knn_model.pkl.gz
with gzip.open("knn_model.pkl.gz", "rb") as f_in:
    with open("knn_model.pkl", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
