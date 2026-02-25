'''Create a Python dictionary representing a user profile with the following fields: name, age, email, is_active, and a list of skills. Convert it to a JSON string using json.dumps() and print it with proper indentation.'''

import json
userProfile = {"name ":"sairam","age":24,"email":"sairam@tail.com","isActive":"True","skills": ["java", "python", "sql", "JavaScript"]}
json.dumps(userProfile)


'''You receive the following mock API response as a JSON string:

{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}
Write Python code to parse this string and print:

The username
The score
A message: "User alex99 scored 87.5 points"'''

response = '{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'
jsonobj = json.loads(response)

username = jsonobj["data"]["username"]
score = jsonobj["data"]["score"]

print("Username:", username)
print("Score:", score)
print(f"User {username} scored {score} points")


'''Given the nested JSON below, extract and print the city and zip code of the user:

{
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}
Then add a new key "country": "India" inside the address and print the updated JSON.

'''

response ='''{
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}'''
jsonobj = json.loads(response)
city =jsonobj["address"]["state"]
pincode= jsonobj["address"]["zip"]
print(city)
print(pincode)
jsonobj["address"]["country"]= "India"
jsonobj=json.dumps(jsonobj,indent=2)
print(jsonobj)
