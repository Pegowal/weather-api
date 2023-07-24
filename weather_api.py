import requests
while True:
    print("\nChoose an option:")
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    BASE_URL = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")

    choice = input("Enter your choice: ")

    if( choice == "0"):
        print("\n------Exiting the program.------\n")
        break
    
    date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")

    if choice == '1':
        if BASE_URL.status_code == 200: 
            data = BASE_URL.json()
            for item in data['list']:
                if item['dt_txt'] == date:
                    print("\n")
                    print(f"Temperature on {date}: {item['main']['temp']} K")
        else:
            print("Error fetching data from the API.")

    elif choice == '2':
        if BASE_URL.status_code == 200:
            data = BASE_URL.json()
            for item in data['list']:
                if item['dt_txt'] == date:
                    print("\n")
                    print(f"Wind Speed on {date}: {item['wind']['speed']} m/s\n")
        else:
            print("Error fetching data from the API.")
    elif choice == '3':
        if BASE_URL.status_code == 200:
            data = BASE_URL.json()
            for item in data['list']:
                if item['dt_txt'] == date:
                    print("\n")
                    print(f"Pressure on {date}: {item['main']['pressure']} hPa\n")
    else:
        print("Invalid choice. Please try again.")