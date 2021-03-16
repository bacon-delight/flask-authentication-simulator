from app import app
from os import urandom


# Application Secret Key
app.config['SECRET_KEY'] = "secret"

# Login Credentials
app.config['CREDENTIALS_USERNAME'] = 'admin'
app.config['CREDENTIALS_PASSWORD'] = 'admin'

# Token Lifetime in Minutes
app.config['ACCESS_TOKEN_LIFETIME'] = 15
app.config['REFRESH_TOKEN_LIFETIME'] = 60

# Token Hashing Algorithm
app.config['ENCRYPT_ALGORITHM'] = 'HS256'

# Token Issuer Information
app.config['TOKEN_ISSUER'] = 'vue-summit-2021:geekle.us'