# Example Settings File

# In this file, we have dummy variables for secret things you'll use in the
# various notebooks in this repo. There are sections for each notebook that
# uses them. If you're note using a particular notebook, you won't need to
# modify the settings in its section.

# If you don't want to mess with this, you can also follow the comments in
# the notebook you want to use to directly enter your secrets in the code.
# We decided to use a settings file to hide our secrets during presentations.

# =============================================================================
# Port Authority TrueTime API
# for notebook port-authority-example.ipynb
# =============================================================================
# You can get your own key by setting up an account at
# http://truetime.portauthority.org/bustime/login.jsp.
# Port Authority will email you an API key after you create the account.
TRUE_TIME_API_KEY = 'a25characterAPIkey0101010'

# =============================================================================
# Domino's Pizza API
# =============================================================================
DEFINITELY_NOT_MY_CREDIT_CARD = {
    "Type": 'CreditCard',
    "Number": "XXXXXXXXXXXXXXX",  # your CC number
    "CardType": "DISCOVER",  # your card type (VISA|MASTERCARD|AMEX|DINERS|DISCOVER|JCB)
    "Expiration": "0222",  # your expiration date MMYY
    "SecurityCode": "445",  # your security code
    "PostalCode": "15206"  # your zip code
}

MY_PERSONAL_INFO = {
    'address': '111 Main Street, Pittsburgh, PA, 15213',  # Put a comma between each item (even address and city)
    'firstName': 'Steven',
    'lastName': 'Saylor',
    'phone': '5555555555',  # I've only tested this without the dashes, so I recommend using that format
    'email': 'steve@youdoyou.boo'
}


#==============================================================================
# Twitter API
#==============================================================================
# To get these keys:
# 1. Make a Twitter account
# 2. Sign up at https://dev.twitter.com for a developer account
#     a. Ensure it has read/write access
# 3. Make an new app under your development account
# 4. Generate an access token key pair
#
# Then you can replace these fake values with the real ones for your account.
TWITTER_KEYS = {
  "access_token_key": "acCe5s70kEn",
  "access_token_secret": "acCe5s70kEn53crEt",
  "consumer_key": "c0n5uM3rk3Y",
  "consumer_secret": "c0N5um3r53cR3t"
}