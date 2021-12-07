from datetime import datetime


def main():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            delta = datetime.strptime(date, "%Y-%m-%d")
            if delta > datetime.today():
                raise ValueError
        except ValueError:
            print("Invalid date. Try again.\n")
        else:
            break
    # print(date)


if __name__ == '__main__':
    main()
