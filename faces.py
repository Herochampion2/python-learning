def main():
    x=input("enter a string ")
    print(convert(x))

def convert(emo):
    emo=emo.replace(":)","🙂").replace(":(","🙁")
    return emo

main()
