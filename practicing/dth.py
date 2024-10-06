def decimalToHex(decimal):
    # Convert decimal to hex
    hex_string = ""
    if decimal == 0:
        hex_string = "00"
    else:
        # Create a lookup table for binary to hex
        binary_to_hex = {
            "0000": "0", "0001": "1", "0010": "2", "0011": "3",
            "0100": "4", "0101": "5", "0110": "6", "0111": "7",
            "1000": "8", "1001": "9", "1010": "A", "1011": "B",
            "1100": "C", "1101": "D", "1110": "E", "1111": "F",
        }

        # Convert decimal to binary manually
        binary = ""
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2

        # Pad binary to ensure length is a multiple of 4
        while len(binary) % 4 != 0:
            binary = "0" + binary

        # Split binary into groups of 4 and convert to hex
        for i in range(0, len(binary), 4):
            four_bits = binary[i:i + 4]
            hex_string += binary_to_hex[four_bits]

    # Ensure the hex string is always 2 characters long
    if len(hex_string) == 1:
        hex_string = "0" + hex_string

    return hex_string

print(decimalToHex(45))