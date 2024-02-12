import tweepy

consumer_key="ooYkCWlY1Q4K9fclO18EeLBWE"
consumer_secret="SMxSJhrfosmcZMe2qK50fbF2zceXeKdyYi4XQWZZDdqgI4oXVW"
access_token="1438868102968643585-aYdpkquXgZ30HUwTKULddoAHH8BaEq"
access_token_secret="BcRsAOi97QOYqSb38Ct7LSZJIQTRs6NZ0Ekgv1EigtQtq"

#autenticar
auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# api objeto
api= tweepy.API(auth)

#postear
api.update_status("Hola, soy un bot de twitter")

