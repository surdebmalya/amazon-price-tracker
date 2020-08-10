from src import strs as s
import streamlit as st
import requests
from bs4 import BeautifulSoup
import smtplib
import time

gmail_id = 'surd5555@gmail.com'
password = 'fsjkpbjefndwwzlq'

def check_price(url, user_price_float, user_mail_id):
	try:
		page = requests.get(url, headers=s.headers)
		soup = BeautifulSoup(page.content, 'html.parser')
		c_price_string = soup.find(id="priceblock_ourprice")
		try:
			if c_price_string==None:
				c_price_string = soup.find(id="priceblock_dealprice").get_text()
			else:
				c_price_string = c_price_string.get_text()
		except:
			return False
		countable_features = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
		final_price_str = ''
		for i in range(len(c_price_string)):
			if c_price_string[i] not in countable_features:
				pass
			else:
				final_price_str+=c_price_string[i]

		current_price = float(final_price_str)
		if (current_price <= user_price_float):
			send_mail(url, user_price_float, user_mail_id)
			return False
		else:
			return True
	except:
		return False

def send_mail(url, user_price_float, user_mail_id):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login(gmail_id, password)

	subject = f"Yooo!!! Price fell down and it's below {user_price_float}"
	body = 'Check The Link Below : \n' + url
	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		gmail_id,
		user_mail_id,
		msg
		)
	server.quit()

def main(url, user_price_float, user_mail_id):
	st.markdown(
		s.confirmation,
		unsafe_allow_html=True,
	)
	running = True
	while running:
		running = check_price(url, user_price_float, user_mail_id)
		time.sleep(60*60)