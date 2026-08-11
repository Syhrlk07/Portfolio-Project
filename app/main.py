import os
import re
import webbrowser

def print_header():
    print("=" * 40)
    print("        CONTENT RESEARCH ENGINE")
    print("=" * 40)
    print()


def load_collections():
    folder = "research"

    collections = os.listdir(folder)

    collections = [
        item for item in collections
        if item != "other"
    ]

    return collections


def load_files(collection):
    folder = os.path.join("research", collection)
    return os.listdir(folder)


def load_experts_files(collection, expert):
    folder = os.path.join("research", collection, expert)
    return os.listdir(folder)


def show_collections(collections):
    print("Knowledge Base Loaded Successfully!\n")

    print("Repository : Portfolio Project\n")

    print("Collections Found:\n")

    for index, collection in enumerate(collections, start=1):
        print(f"{index}. {collection}")

        print()


def choose_collection():
    collections = load_collections()

    show_collections(collections)

    while True:
        choice = input("Choose a collection: ")

        try:
            collection_index = int(choice) - 1

            if collection_index < 0 or collection_index >= len(collections):
                print("Enter the correct number.")
                continue

            break

        except ValueError:
            print("Please enter a number.")

    selected_collection = collections[collection_index]

    print(f"\nSelected Collection: {selected_collection}")

    collection_path = os.path.join("research", selected_collection)

    return selected_collection, collection_path


def choose_expert(selected_collection):
    items = load_files(selected_collection)

    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

    while True:
        expert_choice = input("\nChoose an expert:  ")

        try:
            expert_index = int(expert_choice) - 1

            if expert_index < 0 or expert_index >= len(items):
                print("Enter the correct number.")
                continue

            break

        except ValueError:
            print("Please enter a number.")
    
    selected_expert = items[expert_index]

    print(f"\nSelected Expert: {selected_expert}")

    return selected_expert


def choose_research_file(selected_collection, selected_expert):
    expert_files = load_experts_files(selected_collection, selected_expert)
    
    for index, expert_file in enumerate(expert_files, start=1):
        print(f"{index}. {expert_file}")

    while True:
        file_choice = input("\nChoose a research file: ")

        try:
            file_index = int(file_choice) - 1

            if file_index < 0 or file_index >= len(expert_files):
                print("Enter the correct number.")
                continue

            break

        except ValueError:
            print("Please enter a number.")

    selected_file = expert_files[file_index]
    
    print(f"\nSelected Research File: {selected_file}")

    return selected_file


def read_research(selected_collection, selected_expert, selected_file):
    file_path = os.path.join(
        "research", 
        selected_collection, 
        selected_expert, 
        selected_file
    )

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print(content)

    images = re.findall(r"!\[.*?\]\((.*?)\)", content)

    print("\nImages Found:")
    print(images)

    for image in images:
        webbrowser.open(image)

    print("\n --- END OF RESEARCH ---")


def read_file(file_path):
    print("Opening file...")

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print(content)


def main():
    while True:
        print_header()

        selected_collection, collection_path = choose_collection()

        if os.path.isfile(collection_path):
            read_file(collection_path)
            
            input("\nPress enter to continue...")
            continue

        if os.path.isdir(collection_path):
            print("List of all expert folders:")

        selected_expert = choose_expert(selected_collection)

        selected_file = choose_research_file(
            selected_collection,
            selected_expert
        )

        read_research(
            selected_collection,
            selected_expert,
            selected_file
        )

        input("\nPress Enter to continue...")

main()