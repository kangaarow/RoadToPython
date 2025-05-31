def main():
    file = input("enter the file name:").lower().strip()
    if (file.endswith(".jpg") or file.endswith(".jpeg")):
        print("image/jpeg")
    elif (file.endswith(".txt")):
        print("text/plain")
    elif (file.endswith(".pdf")):
        print("application/pdf")
    elif (file.endswith(".zip")):
        print("application/zip")
    elif (file.endswith(".png")):
        print("image/png")
    elif (file.endswith(".gif")):
        print("image/gif")
    else :
        print("application/octet-stream")

main()


