from openai import OpenAI

client = OpenAI()

# GPT-4 TASKS

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are an HR analyst, you will analyze the metrics, projects, certifications, education and courses taken by a given potential applicant."},
    {"role": "user", "content": "I graduated from Mathematics and Computer Science at Transylvania Univcersity of Brasov, what certifications would you recommend me to take?"}
  ]
)

print(completion.choices[0].message)

# Images

#from openai import OpenAI

#client = OpenAI()

#response = client.images.generate(
#  prompt="A cute baby sea otter",
#  n=2,
#  size="1024x1024"
#)

#print(response)
