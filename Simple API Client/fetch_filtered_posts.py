import requests
import json


def url_request_function(url):
    print(url)
    user_id_to_filter = 1  # You can change this to any usrId

    try:
        # Step 2: Make a GET request to fetch data from the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx/5xx)

        # Step 3: Parse JSON response
        all_posts = response.json()

        # Step 4: Filter posts by userId
        filtered_posts = [post for post in all_posts if post["userId"] == user_id_to_filter]

        # Step 5: Save the filtered posts to a JSON file
        output_filename = f"filtered_posts_user_{user_id_to_filter}.json"
        with open(output_filename, "w") as f:
            json.dump(filtered_posts, f, indent=4)

        print(f"Filtered posts saved to {output_filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        
url_request_function(url="https://jsonplaceholder.typicode.com/posts")
url_request_function(url="https://abc.com")


