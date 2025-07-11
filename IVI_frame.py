
def decode(signal):
    payload = "60 20 45 6C FE 3D 4B AA 40 12 6C AF 05 78 4A 04"
    #signal_map = {"PassengerSeatMemoRequest": [5, 3, 1],
                 # "ClimFPrightBlowingRequest": [5, 7, 7],
                 # "TimeFormatDisplay": [5,3,1]}

    signal_map ={ "PassengerSeatMemoRequest" : { "byte_index":0 , "bit_offset":7, "size":3},
                  "ClimFPrightBlowingRequest" : {"byte_index":5 , "bit_offset":7, "size":4},
                  "TimeFormatDisplay" : {"byte_index":5 , "bit_offset":7, "size":7}}

    if signal not in signal_map:
        print(f" Signal {signal} not found")
        return None

    hex_payload = payload.strip().split()
    int_string = [int(bits, 16) for bits in hex_payload]
    bits_string = [format(bits,'08b') for bits in int_string]

    for i , bits in  enumerate(bits_string):
        print  (f" Byte {i} bits: {' '.join(bits)}")
        #print(f"Byte {i} bits:'', *bits")


    byte_index, bit_offset, size = signal_map[signal]
    byte_index = signal_map[signal]["byte_index"]
    bit_offset = signal_map[signal]["bit_offset"]
    size = signal_map[signal]["size"]
    bit_offset = 7 - bit_offset

    bytes_bits = bits_string[byte_index]

    signal_bits = bytes_bits[bit_offset:bit_offset + size]
    print(f"Signal bits are: {signal_bits}")
    signal_value = int(signal_bits,2) 

    print(f"Semnalul are valorile decimale: byte_index {byte_index}, bit_offset{bit_offset}, size{size}, signal_value{signal_value}")
    return signal_value


result = decode("ClimFPrightBlowingRequest")
print(result)






