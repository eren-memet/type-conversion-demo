""" 
   müşteri adı 
      "    soyadı
      "  ad+soyad
      "cinsiyet
      "tc kimlik
      " birthday
      " address
      " age

"""
customerName = 'Ali'
customerSurname = 'Yılmaz'
customerNameSurname = customerName + ' ' + customerSurname
customerSex = True # Erkek
customerId = '135615166'
customerBirthDate = 1990
customerAddress ='Istanbul Kadıköy'
customerAge = 2010 - customerBirthDate

""" 

2-Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

           Sipariş 1 =>110 TL 
           Sipariş 2 => 1100.5 TL
           Sipariş 3 => 356.95 TL

"""
order1 = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3

print("Total:",total)