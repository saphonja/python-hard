from twilio.rest import TwilioRestClient

account_sid = "AC6340901abc08c7488e64e9d106b97586" # Your Account SID from www.twilio.com/console
auth_token  = "31e4a463815864728b936d007874f74f"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(body="Hello from Python",
    to="+375296909346",    # Replace with your phone number
    from_="8155528062") # Replace with your Twilio number

print(message.sid)
