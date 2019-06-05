from datetime import datetime
import pandas as pd
from flask import Flask, request, render_template, redirect
import transactions
import models

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def showTransactions():

	tx = transactions.initialize()
	portfolio = models.Portfolio()

	# for coin, current_price, quantity in zip(portfolio.coins, portfolio.current_prices, portfolio.quantities):
	# 	temp = df.loc[df['coin'] == coin].reset_index(drop=True)
	# 	cost = temp['cumulative_cost'][len(temp) - 1]
	# 	cost_per_unit = cost/quantity
	# 	unrealised_amt = (current_price - cost_per_unit) * quantity
	# 	realised_amt = sum(temp['gain_loss'].dropna())
	# 	gain_loss = unrealised_amt + realised_amt
	# 	market_val = quantity * current_price
	#
	# 	portfolio.cost.append(cost)
	# 	portfolio.cost_per_unit.append(cost_per_unit)
	# 	portfolio.unrealised_amt.append(unrealised_amt)
	# 	portfolio.realised_amt.append(realised_amt)
	# 	portfolio.gain_loss.append(gain_loss)
	# 	portfolio.market_val.append(market_val)

	transactions = pd.read_csv(TRANSACTIONS_FILE)
	return render_template('../index.html', portfolio=portfolio, transactions=tx)

# Close database connection as soon as an operation is complete
@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()

if __name__ == "__main__":
	app.run(debug=True)
