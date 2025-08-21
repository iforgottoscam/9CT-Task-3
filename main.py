from data_module import (
    display_dataset_preview,
    display_visualisation,
    search_data,
    update_data_entry,
    save_changes,
    load_dataset,
    get_available_datasets
)
import time
def main_menu():
    available_datasets = get_available_datasets()
    
    while True:
        print("\n=== Data Viewer Interface ===")
        print("1. View dataset")
        print("2. View visualisation")
        print("3. Search or filter data")
        print("4. Update a data entry")
        print("5. Save changes")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            dataset_choice = select_dataset(available_datasets)
            if dataset_choice:
                dataset = load_dataset(dataset_choice)
                display_dataset_preview(dataset, dataset_choice)
                time.sleep(1)
        elif choice == '2':
            dataset_choice = select_dataset(available_datasets)
            if dataset_choice:
                dataset = load_dataset(dataset_choice)
                display_visualisation(dataset, dataset_choice)
        elif choice == '3':
            dataset_choice = select_dataset(available_datasets)
            if dataset_choice:
                dataset = load_dataset(dataset_choice)
                search_data(dataset, dataset_choice)
        elif choice == '4':
            dataset_choice = select_dataset(available_datasets)
            if dataset_choice:
                dataset = load_dataset(dataset_choice)
                dataset = update_data_entry(dataset, dataset_choice)
        elif choice == '5':
            dataset_choice = select_dataset(available_datasets)
            if dataset_choice:
                dataset = load_dataset(dataset_choice)
                save_changes(dataset, dataset_choice)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose 1-6.")

def select_dataset(available_datasets):
    """Let user choose which dataset to work with"""
    print("\nAvailable datasets:")
    for i, (filename, exists) in enumerate(available_datasets.items(), 1):
        status = "✓" if exists else "✗"
        print(f"{i}. {filename} {status}")
    
    try:
        choice = int(input("Select dataset (number): ").strip())
        filenames = list(available_datasets.keys())
        if 1 <= choice <= len(filenames):
            selected_file = filenames[choice-1]
            if available_datasets[selected_file]:
                return selected_file
            else:
                print("This dataset file doesn't exist yet.")
                return None
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

if __name__ == "__main__":
    main_menu()