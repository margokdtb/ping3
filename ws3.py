print("\n\n SCAN CLOUDFLARE PORT 80 443\n")

import os

#scan ws port 80
os.system("python ws80.py" )
os.system("python wsssl.py" )
#import ws80
#import wsssl

print("\n\n HASIL DISIMPAN : \n") 
print(" - >> hasil_cdnssl443_ping.txt \n")



