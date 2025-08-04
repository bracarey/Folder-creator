import os


def create_folders(folder_names):
    for name in folder_names:
        try:
            os.makedirs(name, exist_ok=True)
            print(f"Created/Verified folder: {name}")
        except OSError as error:
            print(f"Error creating folder '{name}': {error}")


if __name__ == "__main__":
    print("Enter folder names (separated by spaces):")
    user_input = input().strip()

    if not user_input:
        print("No folder names provided!")
    else:
        folder_list = user_input.split()
        create_folders(folder_list)