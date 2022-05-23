import requests
import json

def question():
    i = 0
    while i < 2:
        answer = input("Question? (Util information? yes or no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            print("Thanks for your time!!!")
            break
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            print("No")
            break
        else:
            i += 1
            if i < 2:
                print('Please enter yes or no')
            else:
                print("Nothing done")




x = input("Enter your name:")
print("write the IP to went search information, " + x)
# URL de la API
api_url = "http://ip-api.com/json/"

# Definimos los parametros de respuesta que queremos obtener
parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {"fields":parametros}

def ip_scraping(ip=""):
 # Nos conectamos con la API
 res = requests.get(api_url+ip, data=data)
 # Obtenemos y procesamos la respuesta JSON
 api_json_res = json.loads(res.content)
 return api_json_res

if __name__ == '__main__':
 # Solicitamos la entrada
 ip = input("Ingrese la dirección IP: ")
 
 # Llamamos a la función ip_scraping y mostramos los resultados
 par = parametros.split(",")
 for x in par:
  print(x.upper(), ":")
  print(ip_scraping(ip)[x])
  print("-----------------------------" , x)
 
 #parte de arriba
 question()
