# code generator
# take input text
# generate cypher from input


while True:
    user_string = input("enter a string to encrypt: ")

    def encrypt(user_string):
        encoded_string = user_string.encode(encoding="AES256")
        print(encoded_string)


#    decode_y_n = input("would you like to decode this string (y/n)? ")
#    if decode_y_n == "y":
#        decoded_string = encoded_string.dec
