dec = {
    "address": {
        "public-key":"PK",
        "private-key":"SK"
    }
}

# publicKey = dec["address"]["public-key"]
# print(publicKey)

address2 = {
    "public-key":"PK2",
    "private-key":"SK2"
}
dec["address2"] = address2

print(dec)