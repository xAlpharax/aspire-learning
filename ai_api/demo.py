### Assuming we have queried the user data into a "random_id.json" file

### LLM INITIALIZATION

from openai import OpenAI

client = OpenAI()

### Parsing user datagrams

import json

with open("random_id.json", "r") as f:
    student_data = json.load(f)

    print("Description: " + student_data["description"])
    print("Passions: " + student_data["passions"])

    # GPT-4 TASKS

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an HR analyst, you will analyze the metrics, projects, certifications, education and courses taken by a given potential applicant."},
            {"role": "user", "content": f"I have a Batchelor in Mathematics and Computer Science from Transylvania University of Brasov. I have this description: {student_data['description']} and these passions: {student_data['passions']}. What jobs should I be looking for on this platform ?"},
        ]
    )

    print(completion.choices[0].message)
