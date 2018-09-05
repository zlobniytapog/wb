import requests
from bs4 import BeautifulSoup

header = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
'Cache-Control' : 'no-cache',
'Connection' : 'keep-alive',
'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
'cookie': "__ver=5247; mobile_client=0; __store=686_1733_1193_507; __region=38_31_1_4_22_33_39_30_45_42_40; __pricemargin=1,0; wb_yadirect=not.set; _ga=GA1.2.47161988.1536128752; _gid=GA1.2.192016853.1536128752; criteo_uid=BEGCmh70nx2EtZhDFiPlxkdpzKXiM1VC; ___wbuV1=userId=7849dcca-ada1-4157-b844-4b540e4cba3b&firstVisit=09/05/2018%2006:25:56&lastVisit=09/05/2018%2006:29:45; ___wbs=sessionId=fa34b5e5-1e19-4e32-bc0f-ab412527c555&startDateTime=09/05/2018%2006:25:56; ASP.NET_SessionId=3alhc2xcnt0yqvwkyeywhfns; __RequestVerificationToken=xmj9B0qvoTfu1RCnRJ9C5TjKRN14llDdZtQgoXdNJh8PJvMv8vJ3KemTm43BwkJvlrcTGKwbJ-itYq1v268clD1BkCU1; __bsa=basket-ru-8; _dc_gtm_UA-2093267-1=1; __wbl=cityId=5618&regionId=54&city=%d0%9d%d0%be%d0%b2%d0%be%d1%81%d0%b8%d0%b1%d0%b8%d1%80%d1%81%d0%ba&phone=83833121150&latitude=55,02583&longitude=82,91935; BasketUID=6a70855a-c5ad-454c-baae-34b382eff896",
'host' : 'security.wildberries.ru',
'pragma' : 'no-cache',
'Referer' : 'https://security.wildberries.r…s.ru&xdm_c=default9852&xdm_p=1',
'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
'x-requested-with': 'XMLHttpRequest'
}