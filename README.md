# Interner_Crawler
## 20180601
### A problem that scrapy can't be installed occured.
##### There is an error message below:
```
Failed building wheel for cryptography
```

##### And I try this command
```
pip3 install cryptography
```

##### But it still ouputs the same message
```
Failed building wheel for cryptography
```

##### Finally I find this article:
```
https://stackoverflow.com/questions/22073516/failed-to-install-python-cryptography-package-with-pip-and-setup-py
```
##### And I try this command
```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```

##### After it completes,I can install the "cryptography" successfully
```
pip3 install cryptography
```

##### The "scrapy" is also installed successfully then
```
sudo pip3 install scrapy
```
