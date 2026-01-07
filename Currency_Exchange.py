def exchange_money(budget, exchange_rate):
        """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
        value = budget/exchange_rate
        return value

def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    change=budget-exchanging_value
    return change

def get_value_of_bills(denomination, number_of_bills):
        """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
        val = denomination*number_of_bills
        return val

def get_number_of_bills(amount,denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    no = amount//denomination
    return no

def get_leftover_of_bills(amount,denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    shaft = amount%denomination
    return shaft

def exchangeable_value(budget,exchange_rate,spread,denomination):
    spread_dec = spread/100
    new_exch = exchange_rate*(1+spread_dec)
    new_currency = budget/new_exch
    no_of_bills = new_currency//denomination
    max_value = no_of_bills*denomination
    
    return max_value