class MpesaAccount:
	def __init__(self,name,phone_number,balance):
				self.name=name
				self.phone_number=phone
				self.balance=balance
	def deposit(self,amount):
		self.balance = self.balance + amount
		sms ("Hey {}, you have successfuly deposited Ksh{} into your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance))
		
	def withdraw(self,amount):
		if self.balance>amount:
			self.balance = self.balance - amount
			sms ("Hey {}, you have successfully withdrawn Ksh{} from your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance))
		else:
			sms ("Sorry {}, you have no enough fund in your account to withdrawal. Your current balance is Ksh{}.".format(self.name,self.balance))

	def check_balance(self):
		sms ("Hey {},remaining M-pesa balance is Ksh{}".format(self.name,self.balance))