import os


def print_header():
    print("=" * 40)
    print("        CONTENT RESEARCH ENGINE")
    print("=" * 40)
    print()


def load_collections():
    folder = "research"
    return os.listdir(folder)


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


def main():

    print_header()

    collections = load_collections()

    show_collections(collections)

    choice = input("Choose a collection: ")

    collection_index = int(choice) - 1

    selected_collection = collections[collection_index]

    print(f"\nSelected Collection: {selected_collection}")

    items = load_files(selected_collection)

    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

    expert_choice = input("\nChoose an expert:  ")

    expert_index = int(expert_choice) - 1

    selected_expert = items[expert_index]

    print(f"\nSelected Expert: {selected_expert}")

    expert_files = load_experts_files(selected_collection, selected_expert)

    for index, expert_file in enumerate(expert_files, start=1):
        print(f"{index}. {expert_file}")

    file_choice = input("\n Choose a research file: ")

    file_index = int(file_choice) - 1

    selected_file = expert_files[file_index]

    print(f"\nSelected Research File: {selected_file}")

    file_path = os.path.join(
        "research", 
        selected_collection, 
        selected_expert, 
        selected_file
    )

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print(content)

    print("\n --- END OF RESEARCH ---")
    

main()