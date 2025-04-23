This repo manages API tokens for [OpenRouter](https://openrouter.ai/).

Currently, it is hosted on our [website](https://github.com/uoft-isl/website) at `/projects/TISL_openrouter`. 
A cron script runs every 1st day of the month to call [cron_topup.sh](cron_topup.sh).

The script expects [MANAGEMENT_KEY](MANAGEMENT_KEY) file with provisions API key to be in the folder. 

## Adding users
1. Add row with user's email to [database.csv](database.csv) file.
2. Run [create_tokens.py](create_tokens.py)
3. Send the output to the user.
4. If you lost the output, the token is written to [database.csv](database.csv) file in the last column.

## Changing amount of top up per month:
1. Edit CREDITS_PER_MONTH in [util.py](util.py)
2. ???
3. Profit!