import json

sat_results = []

def insert_data():
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    city = input("Enter City: ")
    country = input("Enter Country: ")
    pincode = input("Enter Pincode: ")
    sat_score = int(input("Enter SAT score: "))

    passed = sat_score > 30

    data = {
        "Name": name,
        "Address": address,
        "City": city,
        "Country": country,
        "Pincode": pincode,
        "SAT score": sat_score,
        "Passed": passed
    }

    sat_results.append(data)
    print("Data inserted successfully.")

def view_all_data():
    print(json.dumps(sat_results, indent=4))

def get_rank():
    name = input("Enter Name: ")
    sorted_results = sorted(sat_results, key=lambda x: x["SAT score"], reverse=True)

    for i, data in enumerate(sorted_results):
        if data["Name"] == name:
            print(f"Rank: {i+1}")
            return
    print("Data not found.")

def update_score():
    name = input("Enter Name: ")
    for data in sat_results:
        if data["Name"] == name:
            sat_score = int(input("Enter new SAT score: "))
            data["SAT score"] = sat_score
            data["Passed"] = sat_score > 30
            print("Score updated successfully.")
            return
    print("Data not found.")

def delete_record():
    name = input("Enter Name: ")
    for data in sat_results:
        if data["Name"] == name:
            sat_results.remove(data)
            print("Record deleted successfully.")
            return
    print("Data not found.")

def print_menu():
    print("\nMenu:")
    print("1. Insert data")
    print("2. View all data")
    print("3. Get rank")
    print("4. Update score")
    print("5. Delete one record")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            insert_data()
        elif choice == "2":
            view_all_data()
        elif choice == "3":
            get_rank()
        elif choice == "4":
            update_score()
        elif choice == "5":
            delete_record()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
