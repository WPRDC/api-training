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
