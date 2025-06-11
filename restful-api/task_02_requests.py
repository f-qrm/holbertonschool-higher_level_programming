#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder API and prints their titles.

    Makes a GET request to the JSONPlaceholder posts endpoint, checks the
    response status code, and if successful (200), iterates through all
    posts to print their titles to the console.

    Args:
        None

    Returns:
        None

    Raises:
        requests.exceptions.RequestException: If the HTTP request fails.

    Example:
        >>> fetch_and_print_posts()
        Status Code: 200
        sunt aut facere repellat provident occaecati excepturi
        optio reprehenderit
        qui est esse
        ea molestias quasi exercitationem repellat qui ipsa sit aut
        ...
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        for title in r.json():
            print(title["title"])


def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder API and saves them to a CSV file.

    Makes a GET request to the JSONPlaceholder posts endpoint and if
    successful (200), creates a CSV file named 'posts.csv' with columns
    for id, title, and body. Each post is written as a row in the CSV.

    Args:
        None

    Returns:
        None

    Raises:
        requests.exceptions.RequestException: If the HTTP request fails.
        IOError: If there's an error creating or writing to the CSV file.

    Note:
        The CSV file will be created in the current working directory.
        If the file already exists, it will be overwritten.

    Example:
        >>> fetch_and_save_posts()
        # Creates posts.csv with id, title, body columns
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        data = r.json()
        with open('posts.csv', 'w', encoding='utf-8') as new_data:
            posts = csv.DictWriter(new_data, ['id', 'title', 'body'])
            posts.writeheader()

            for dict in data:
                posts.writerow({
                    'id': dict['id'],
                    'title': dict['title'],
                    'body': dict['body']
                })
