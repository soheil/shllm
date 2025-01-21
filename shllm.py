import os
import sys
import http.client
import json

def llm(cmd):
  current_directory = os.getcwd()
  files = [f for f in os.listdir(current_directory)]

  api_key = os.getenv('OPENAI_API_KEY')

  # Connection to OpenAI's API
  conn = http.client.HTTPSConnection("api.openai.com")

  # Define the headers, including the authorization and content type
  headers = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {api_key}',
  }

  payload = json.dumps({
      "model": "gpt-4o-mini",
      "messages": [
        {
          "role": "system",
          "content": "you should always only output a single bash one-liner"
        }, {
          "role": "user",
          "content": f'{cmd} - here are the content of the current dir: ${files}',
        }
      ],
  })

  # Make a POST request to the completions endpoint
  conn.request("POST", "/v1/chat/completions", payload, headers)

  # Get the response from the server
  res = conn.getresponse()
  data = res.read()

  response_text = data.decode("utf-8")
  conn.close()

  response_data = json.loads(response_text)
  assistant_response = response_data['choices'][0]['message']['content']


  assistant_response = assistant_response \
    .replace('```bash\n', '') \
    .replace('```\n', '') \
    .replace('```', '') \
    .replace('`', '')

  return assistant_response

if len(sys.argv) > 1:
     user_cmd = sys.argv[1]
     print(llm(user_cmd))
else:
     print("No variable passed")
