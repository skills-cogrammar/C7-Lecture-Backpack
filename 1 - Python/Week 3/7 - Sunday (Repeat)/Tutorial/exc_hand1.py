try:
    f = open('lyrics.txt')
    try:
        f.write("This is to update the file")
    except:
        print("Something went wrong in writing the file")        
    finally:
        f.close()
except:
    print("Something went wrong when opening the file.")               
