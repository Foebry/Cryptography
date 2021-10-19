


def validate(string):
    """
        Validates if the given string is a valid hex_string

        :arg string: hex string to validate
        :type string: str

        :return: str
    """
    validated_string = ""
    i = 0
    letters = ("abcdef")

    while i < len(string):
        letter_first = i%2 == 0 and string[i] in letters
        number = i%2 == 0 and string[i] not in letters and string[i+1] not in letters

        if letter_first:
            validated_string += string[i+1]
            validated_string += string[i]
            i += 2
            continue

        elif number:
            numbers = string[i] + string[i+1]
            value = int(numbers)
            if value > 79:
                validated_string += string[i+1]
                validated_string += string[i]
                i += 2
                continue

            validated_string += string[i]
            i += 1
            continue

        validated_string += string[i]
        i += 1

    return validated_string



def reverse(string):
    """
        Reverses the encoded hex_string.
        Checks if new string is valid.

        :arg string: string to reverse
        :type string: str

        :return: str
    """
    reversed_string = ""

    for char in string: reversed_string += char

    return validate(reversed_string)



def encrypt(data, keyword):
        """
            encrypt the given data.

            :arg data: data to be encrypted
            :type data: str

            :return: str
        """
        if type(data) != str: raise TypeError("Wrong type for data. Make sure you pass a string to encrypt")

        # Convert to binary
        new_string = data.encode("utf-8").hex()
        # reverse
        new_string = reverse(new_string)
        # paste behind keyword in bytes
        return keyword.encode("utf-8").hex() + new_string



def decrypt(data, keyword):
    """
        decrypt the given data to the original data.

        :arg data: data to be decrypted
        :type data: str

        :return: str
    """
    if type(data) != str: raise TypeError("Wrong type for data. Make sure you pass a string to encrypt")

    # check if hex keyword in data
    encoded_keyword = keyword.encode("utf-8").hex()
    if encoded_keyword not in data:
        return data

    data = data.replace(encoded_keyword, "")

    reversed = reverse(data)

    original = bytes.fromhex(reversed).decode("utf-8")

    return original
