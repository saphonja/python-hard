from twilio.rest import TwilioRestClient

account_sid = "AC6670a55ffca7cec0e49e13f74a2755d0" # Your Account SID from www.twilio.com/console
auth_token  = "70fe51ff8b1b60272c0044ad126323a8"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello again from Python",
    to="+375296909346",    # Replace with your phone number
    from_="+18155528062") # Replace with your Twilio number

print(message.sid)
