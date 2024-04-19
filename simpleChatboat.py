dictionay={
    "hii":"hello",
    " how are you ":"yes i am all right",
    "sorry":"sorry",

}
print("""
    welcome in manish-AI chatBoat
            Ask me any query
    """)


while True:
    qs=input()
    if qs=="quick" :
        break
    else:
        print(dictionay[qs])
