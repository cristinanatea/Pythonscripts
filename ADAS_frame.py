def assign(signal, payload, new_value):
    signal_map = {
        "LDW_AlertStatus": [2, 5, 2],
        "DW_FollowUpTimeDisplay": [4, 7, 6],
        "LCA_OverrideDisplay": [5, 2, 1]
    }

    if signal not in signal_map:
        print(f"Signal {signal} not found")
        return None

    hex_payload = payload.strip().split()
    int_string = [int(bits, 16) for bits in hex_payload]
    bits_string = [format(bits, '08b') for bits in int_string]

    for i, bits in enumerate(bits_string):
        print(f"Byte {i} bits: {' '.join(bits)}")

    valid_payload=[]
    for i in range(0,len(bits_string) - 11,12):
        single_payload =bits_string[i:i+12]
        bits = [format(int(b,16), '08b') for b in single_payload]

        header = single_payload[1] + single_payload[2]
        print(f"The header is: {header}")
        DLC = single_payload[3]
        print(f"The DLC is: {DLC}")
        pdus = single_payload[4:12]
        print(f"The pdu is: {pdus}")
        delimiter = single_payload[11]
        print(f"The delimiter is: {delimiter}")

        if DLC == "00001000" and delimiter == "00000000":
            valid_payload.append((i, single_payload))
            print(f"Valid payload is : {valid_payload}")
        else:
            print("Invalid pdu")
            continue

    if signal == "LCA_OverrideDisplay" and len(valid_payload)>=3:
        start_index, target_payload = valid_payload[2]
        print(f"Valid payload 2 is:{valid_payload[2]}")
    elif signal =="DW_FollowUpTimeDisplay" and len(valid_payload)>=2:
        start_index, target_payload = valid_payload[1]
        print(f"Valid payload 1 is : {valid_payload[1]}")
    else:
        start_index, target_payload = valid_payload[0]

    pdus =target_payload[4:12]
    pdu_bits = ''.join(pdus)
    byte_index, bit_offset, size = signal_map[signal]
    bit_offset = 7 - bit_offset
    abs_bit_index = byte_index * 8 + bit_offset

    bits_payload = ''.join(bits_string)

    signal_bits = pdu_bits[abs_bit_index:abs_bit_index + size]
    print(f"Signal bits are: {signal_bits}")
    signal_value = int(signal_bits, 2)

    new_bits = format(new_value, f"0{size}b")


    new_bits_payload = (
    pdu_bits[:abs_bit_index] +
    new_bits +
    pdu_bits[abs_bit_index + size:])



    eight_bits_group_payload = [new_bits_payload[i:i + 8] for i in range(0, len(new_bits_payload), 8)]
    new_hex_payload = [format(int(byte, 2), '02X') for byte in eight_bits_group_payload]


    print(f"Vechiul payload este: {' '.join(hex_payload)}")
    print(f"Noul payload este: {' '.join(new_hex_payload)}")

    return new_hex_payload


result = assign("LCA_OverrideDisplay","00 06 02 08 80 00 00 00 00 00 00 00 00 05 D0 08 FF 60 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 00 00 00 00 10 C7 77 8A 70 AB AF 88 2A 8C 00 06 02 08 40 00 00 10 00 00 00 00 00 05 D0 08 21 20 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 00 00 00 00 00 11 29 FB 84 33 1D E5 5E 9D"
 ,1)
print(result)