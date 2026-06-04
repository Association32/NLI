

##Note from workshop:

# this line is wrong. A bug added to the code
###print(test_combined.size()) # should be torch.Size([32, 400])

####### Added this section to get the files, instead of having to upload them to colab every time



from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import os

with open("results.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)

download_and_unzip("https://raw.githubusercontent.com/Association32/NLI/main/t5-assignment-nli.zip")


try:
  download_and_unzip("https://raw.githubusercontent.com/Association32/NLI/main/t5-assignment-nli.zip")
  print("data files downloaded successfully.")
except Exception as e:
  print(e)

try:

  os.remove("nli.ipynb")
  print("nli.ipynb deleted successfully.")

except Exception as e:
  print(e)


