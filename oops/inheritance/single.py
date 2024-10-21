# accessing one class methods to another class via inheritance

class Dashboard:
    
    def __init__(self):
        pass

    def current_month_total_earning(self, total=0):
        if total:
            print(f"Current month total is: {total} Rs.")
        else:     
            print("There is no total value found this month.")


class AccountDashboard(Dashboard):
    
    def show_opening_bal(self):
        print("Current opening balance is 100 Rs.")

class StockDashboard(Dashboard):

    def show_total_stock(self):
        print("Current opening balance is 1000 Qty.")


# AccountDashboard and StockDashboard both dashboard is need, 
# the current_month_total_earning from Dashboard 
 
ac_dashboard = AccountDashboard()

# AccountDashboard method
ac_dashboard.show_opening_bal()

# Dashboard accessing via ac_dashboard with the inheritance
ac_dashboard.current_month_total_earning(120)