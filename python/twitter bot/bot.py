import tweepy

consumer_key="2SWmATMWKtpDAjMaiYfnjvGnG"
consumer_secret="m4MPLWmgCsrNPcWPNuetnM6UNB4b20k0gpGM0Vf7hfweyjv5uV"
access_token="1438868102968643585-b8iPeAQ0gFiBWPt2lv9PQkWnYDEehP"
access_token_secret="XulHS5stJrn2LZ7krQS7Sb5Vd1AUImW8Q2r5jsr47ZHnl"

#autenticar
auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# api objeto
api= tweepy.API(auth)

#postear
api.update_status("Hola, soy un bot de twitter")

