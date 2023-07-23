print("\n\n SCAN WS PORT 80 \n")

import requests

urls = ['http://api.myxl.xlaxiata.co.id']

proxies = []

# Membaca file hasil2_direct.txt sebagai sumber proxy
with open('hasil2_direct.txt', 'r') as file:
    proxy_list = file.readlines()
    # Menambahkan setiap baris di file sebagai proxy dalam bentuk yang sesuai
    for proxy in proxy_list:
        proxies.append({'http': proxy.strip()})

headers = {
    'Host': 'api.myxl.xlaxiata.co.id',
    'Connection': 'Upgrade',
    'User-Agent': '[ua]',
    'Upgrade': 'websocket'
}

with open('hasil_websocket80.txt', 'w') as hasil_file:
    for proxy in proxies:
        print(f'{proxy["http"]}')
        result = f'{proxy["http"]}\n'
        
        try:
            response = requests.head(urls[0], headers=headers, proxies=proxy, timeout=3)
            
            if response.elapsed.total_seconds() > 3:
                # result += 'timeout\n'
                print('timeout')
                print('----')
                continue
                
            status_code = response.status_code
            
            if status_code == 200:
                #result += f'Kode Respon HTTP: {status_code}\n'
                print(f'Respon : {status_code} Ok')
                
                hasil_file.write(result)

        except:
            result += 'tidak valid, melewati...\n'
            print('tidak valid, melewati...')
        
        #result += '----\n'
        print('----')