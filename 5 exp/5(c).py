from bs4 import BeautifulSoup
with open(path,'r')as f
data=f.read()
Bs_data=BeautifulSoup(data,"xml")
B_unique=Bs_data.findall('unique')
print(B_unique)
B_name=Bs_data.find('child',{'name':'Frank'})
print(B_name)
value=b_name.get('test')
