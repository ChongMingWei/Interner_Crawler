# Interner_Crawler
## 20180601
I meet a problem that scrapy can't be installed.
The error message is like below:
![alt text](https://i.imgur.com/etvQFWg.png)

And I try this command
![alt text](https://i.imgur.com/URixteK.png)

But it still ouputs the same message
![alt text](https://i.imgur.com/etvQFWg.png)

Finally I find this article:
https://stackoverflow.com/questions/22073516/failed-to-install-python-cryptography-package-with-pip-and-setup-py
And I try this command
```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```
![alt text](https://i.imgur.com/m8DN5su.png)
After it completes,I can install the "cryptography" successfully
```
pip3 install cryptography
```
