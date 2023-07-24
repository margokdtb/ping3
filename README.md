# ping3
Scan subdomainya dengan knock

Install termux 
pkg update -y
pkg upgrade -y
pkg install python python-pip git 

#install knock domain finder
git clone https://github.com/guelfoweb/knock.git
cd knock
pip3 install -r requirements.txt
cd
 
#install bugscanner
git clone https://github.com/aztecrabbit/bugscanner
cd bugscanner
pip install -r requirements.txt
cd

#install bugscanner go
pip install golang
go install -v github.com/aztecrabbit/bugscanner-go@latest
echo 'PATH="$PATH:$HOME/go/bin"' >> $HOME/.bashrc && source $HOME/.bashrc

#install menu
cd /sdcard
git clone https://github.com/margokdtb/ping3.git
cd ping3
pip3 install -r requirements.txt

Uses
cd
cd /sdcard/ping3 
python go.py

