import os


def print_header():
    print("=" * 40)
    print("        KIKI RESEARCH AI")
    print("=" * 40)
    print()


def load_collections():
    folder = "research"
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

    if choice == "1":
        print("\nOpening linkedin-posts...")

    elif choice == "2":
        print("\nOpening other...")

    elif choice == "3":
        print("\nOpening sources...")

    elif choice == "4":
        print("\nOpening youtube-transcripts...")


main()