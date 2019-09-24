sudo apt-get install -y python3-pip python-pip git libcurl4-openssl-dev python-pycurl python3-requests python-requests
sudo pip3 install -r requirements.txt
cd ~
git clone https://github.com/jayvdb/urllib4.git
cd urllib4
sudo chmod +x ez_setup.py
sudo python ez_setup.py
sudo chmod +x setup.py
sudo python setup.py build && sudo python setup.py install
