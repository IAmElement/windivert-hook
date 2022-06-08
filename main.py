from pydivert import WinDivert

def main():
    patched = False 
    with WinDivert('tcp.SrcPort == 8080') as packets: # As soon as packets hit 8080, this begins
        for packet in packets: 
            if packet.src_addr == '74.91.122.149' and b'm_success' in packet.tcp.payload:
                packet.tcp.payload = b'\x82w\x85\xa9m_success\xc3\xa9m_message\xd9;Thank you for using desudo!................................\xa6m_key0\xce\tv\xa62\xa6m_key1\xce\t\xb2\xe2\x04\xa6m_key3\xce\x00\xcfG\xc7' # Injected return data for bypass
                patched = True
            packets.send(packet) # Send the payload
            if patched is True:
                print('Packet spoofed!')
                exit()

try:
   main()
except Exception as e:
    print(f'ERROR: {e}')
