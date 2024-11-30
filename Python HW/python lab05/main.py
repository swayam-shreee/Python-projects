import weather 
import json

def main():

    filename = 'w.dat'
    weather_data = {}

    while True:
        # Display the menu
        print("\n*** TUFFY TITAN WEATHER LOGGER MAIN MENU")
        print("1. Set data filename")
        print("2. Add weather data")
        print("3. Print daily report")
        print("4. Print historical report")
        print("9. Exit the program\n")

        choice = input("Enter menu choice: ")
        print("")

        if choice == "1":
            # Set data filename
            filename = input("Enter data filename: ")
            weather_data = weather.read_data(filename=filename)

        elif choice == "2":
            # Add weather data
            date = input("Enter date (YYYYMMDD): ")
            time = input("Enter time (hhmmss): ")
            temperature = int(input("Enter temperature: "))
            humidity = int(input("Enter humidity: "))
            rainfall = float(input("Enter rainfall: "))

            datetime_key = date + time

            # Add the weather reading to the dictionary
            weather_data[datetime_key] = {'t': temperature, 'h': humidity, 'r': rainfall}

            # Write updated data back to the file
            weather.write_data(data=weather_data, filename=filename)

        elif choice == "3":
            # Print daily report
            date = input("Enter date (YYYYMMDD): ")
            report = weather.report_daily(data=weather_data, date=date)
            print(report)

        elif choice == "4":
            # Print historical report
            report = weather.report_historical(data=weather_data)
            print(report)

        elif choice == "9":
            # Exit the program
            print("Exiting the program...")
            break

        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()