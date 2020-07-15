# nextpoint
V. 0.01
I decided to learn BS4 during such a damn quarantine.
so, please don't kill me. I realize all mistakes in this code. 
as an example, I don't care about months. Data start from September and finished April, but all set choices from Jan to Dec each year (hardcoded) :)

At the first stage, I parsing the site https://minfin.com.ua/ and extract data.
exact link on the historic data is(view.py - row 9):
URL = 'https://minfin.com.ua/currency/mb/archive/usd/20-09-2005/23-04-2020/'
extracted data saved into db.
Then you can choose the Year and see charts for any month.
Enjoy :)

In case you wanna extract data again. drop db, or at least delete all data from table:
delete from currency_usd
Then you can use the link to populate db: 
127.0.0.1/dic/
It can take about 1-2 minutes
