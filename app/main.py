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


def get_valid_choice(options):
    while True:
        choice = input()

        try:
            index = int(choice) - 1

            if index < 0 or index >= len(options):
                print("Enter the correct number.")
                continue

            return index
        
        except ValueError:
            print("Please enter a number.")


def choose_collection():
    collections = load_collections()

    show_collections(collections)

    collection_index = get_valid_choice(collections)

    selected_collection = collections[collection_index]

    print(f"\nSelected Collection: {selected_collection}")

    collection_path = os.path.join("research", selected_collection)

    return selected_collection, collection_path


def choose_expert(selected_collection):
    items = load_files(selected_collection)

    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

    expert_index = get_valid_choice(items)
    
    selected_expert = items[expert_index]

    print(f"\nSelected Expert: {selected_expert}")

    return selected_expert


def choose_research_file(selected_collection, selected_expert):
    expert_files = load_experts_files(selected_collection, selected_expert)
    
    for index, expert_file in enumerate(expert_files, start=1):
        print(f"{index}. {expert_file}")

    file_index = get_valid_choice(expert_files)

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