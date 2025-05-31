def main():
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    while True:
        date = input("Date: ")
        try:
            if '/' in date:
                month,day,year= date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if 1<=month<=12 and 1<=day<=31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
                continue
            elif ',' in date:
                parts = date.split()
                if len(parts) == 3:
                    month_str= parts[0]
                    day = int(parts[1].replace(',',''))
                    year = int(parts[2])
                    if month_str in months and 1<=day<=31:
                        month = (months.index(month_str)) + 1
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
                    continue
        except (ValueError,IndexError):
             pass

if __name__ == "__main__":
    main()


