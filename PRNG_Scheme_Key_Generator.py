# Initializing variables
  # n is 5 in binary
iv = 0b01101101  # iv is 0 in binary
initial_list = [
    0b00000101, 0b00000010, 0b00000001, 0b10000000, 0b01000000,
    0b10100000, 0b11010000, 0b11101000, 0b11110100
]

# Loop 1: Until iv reaches 11111111
j = 1
n_list = []  # To store results of each loop iteration
n = 0b00000101

# Loop 2: 9 iterations
while j <= 40:
        # Add n to n_list
        n_list.append(n)

        # XOR bits of n that are '1' with the corresponding bits of iv
        xor_value = 0
        for i in range(8):  # 8 bits in total
            if (n >> i) & 1:  # Check if the i-th bit of n is 1
                xor_value ^= (iv >> i) & 1  # XOR with the corresponding bit of iv

        # Shift n one place to the right and add the XOR result
        n = (n >> 1) | (xor_value << 7)  # Shift n right and place XOR result at MSB

        j += 1  # Increment j

    # Compare n_list with the initial_list
if n_list == initial_list:
    print(f"Match found with iv = {hex(iv)}")

    # Print n_list and iv in hex
print([hex(x) for x in n_list])

    # Increment iv
iv += 1