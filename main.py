from src import widget

account_details = str()
time_event = str()

widget.mask_account_card(account_details)
widget.get_date(time_event)

transactions: list[dict] = []
state = ()
sort = ()

processing.filter_by_state(transactions, state)
processing.sort_by_date(transactions, sort)

