import os


def load_towns(path):
    dir = "../traveler_project/data"
    full_path = os.path.join(dir, path)
    with open(full_path, "r") as file:
        contents = file.read().splitlines()  # creating a list of 'Town, X, Y'
        town_details = [
            tuple(content.split()) for content in contents
        ]  # convertint the string 'Town X, Y' into a tuple ('Town, X, Y')
        return town_details


if "__name__" == "__main__":
    load_towns("towns.txt")
