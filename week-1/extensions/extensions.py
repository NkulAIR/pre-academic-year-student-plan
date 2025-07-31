def many_dots():
    name = file_name.split(".", 2)
    extension = name[2]
    return extension


formats = {".gif" : "image/gif",
            ".jpeg" : "image/jpeg",
            ".jpg" : "image/jpeg",
            ".png" : "image/png",
            ".pdf" : "application/pdf",
            ".txt" : "text/plain",
            ".zip": "application/zip"}

file_name = input("Filename: ").strip(" ").lower()
name = file_name.split(".")


if file_name.count(".") > 1:
    extension = many_dots()
    name = file_name.split(".")
    match extension:
        case "gif":
            print(formats[".gif"])
        case "jpeg" | "jpg" :
            print(formats[".jpeg"])
        case "png":
            print(formats[".png"])
        case "pdf":
            print(formats[".pdf"])
        case "txt":
            print(formats[".txt"])
        case "zip":
            print(formats[".zip"])
        case _:
            print("application/octet-stream")

elif file_name.count(".") == 1:
    name = file_name.split(".")
    extension = name[1]
    match extension:
        case "gif":
            print(formats[".gif"])
        case "jpeg" | "jpg" :
            print(formats[".jpeg"])
        case "png":
            print(formats[".png"])
        case "pdf":
            print(formats[".pdf"])
        case "txt":
            print(formats[".txt"])
        case "zip":
            print(formats[".zip"])
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")
