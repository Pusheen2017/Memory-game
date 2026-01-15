while True:
    code=str(input(">>>"))
    try:
        exec(code)
    except:
        print("Error")