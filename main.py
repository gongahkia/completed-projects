from budget_app import Category
from budget_app import create_spend_chart

entertainment = Category ('Entertainment')
business = Category ('Business')
Food = Category ('Food')
Mickey = Category ('Gabriel Ong Zhe Mian')
Mickey.deposit (500, 'ok')
business.deposit (100, 'mcdonalds')
entertainment.deposit (20, 'learning lab')
entertainment.deposit (50, 'chicken rice')
entertainment.withdraw (60, 'itsoverforyoufoolsonceigetbuttimplants')
entertainment.transfer (2, business)
Mickey.withdraw(400, 'help lah')
business.withdraw (100, 'test me more')
Mickey.get_balance()
"""entertainment.get_balance()
business.get_balance()
print(business.check_funds(200))
print (business)
print (Food)
print (Mickey)"""
create_spend_chart([business, entertainment, Food, Mickey])
