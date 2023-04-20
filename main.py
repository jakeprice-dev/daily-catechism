import json
import requests
import yaml

# Load Configuration File:
with open("config.yml", "r", encoding="utf-8") as config:
    config = yaml.safe_load(config)

# Variables:
gotify_app_token = config["gotify_app_token"]
gotify_base_url = config["gotify_base_url"]
catechism_file = config["catechism_file"]
catechism_questions = config["catechism_questions"]

# Load Catechism File:
with open(catechism_file, "r", encoding="utf-8") as catechism:
    catechism = yaml.safe_load(catechism)

# Load Tracker file:
with open("tracker.txt", "r", encoding="utf-8") as tracker:
    # Read the previous question number:
    previous_question = tracker.read().strip()

    # Extract previous question number:
    previous_question_number = int(previous_question.strip("Question_"))

    # Calculate the next question number based on the previous:
    if previous_question_number >= catechism_questions:
        next_question_number = 1
    else:
        next_question_number = previous_question_number + 1

    # Create the next question text for the tracker file:
    next_question = f"Question_{next_question_number}"


# Loop through all the catechism questions:
for question_number, qa_dict in catechism["Questions"].items():
    # Which catechism are we running through:
    catechism_name = catechism["Catechism_Name"]

    # Extract the question and answer from the current question:
    question = qa_dict["Question"]
    answer = qa_dict["Answer"]
    references = qa_dict["References"]

    if next_question == question_number:
        # Gotify API Configuration:
        api_url = f"/message?token={gotify_app_token}"

        # Setup the notification message:
        api_payload = {
            "priority": 4,
            "title": catechism_name,
            "message": f"""
### Question {next_question_number} - {question}

> {answer}

{references}
""",
            "extras": {
                "client::display": {"contentType": "text/markdown"},
            },
        }

        # Create the API endpoint:
        api_endpoint = gotify_base_url + api_url

        # Post the message to the Gotify API (send the catechism notification):
        response = requests.post(
            api_endpoint,
            headers={"Content-Type": "application/json"},
            json=api_payload,
            timeout=300,
        )

        # Stop the loop:
        break

# Update the tracker file:
with open("tracker.txt", "w", encoding="utf-8") as tracker:
    # Start again once we've reached the final question:
    if previous_question_number >= catechism_questions:
        tracker.write("Question_1")
    # Otherwise just write the next question to the tracker file:
    else:
        tracker.write(next_question)
