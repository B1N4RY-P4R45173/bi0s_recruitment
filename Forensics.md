# Network Forensics
## Process:
Unzipped the file to get the .pcap.

Opened it with Wireshark.

Went through the packets and at the 5th Serial number there was a message stating the key was 5.

The I went through the rest of the packets and there I found a suspected string which supposedly looks like the flag and that was `gn0x{s3yb0wp_nsyjwhjuynts_l0jx_g00rc0c0}?` after using a ceaser cipher with a shift of 5 letters I found the flag.

## Flag Found 
`bi0s{n3tw0rk_interception_g0es_b00mx0x0}`

# Steganography
## Process:
### Method- 1
This can be done by using stegsolve usin the inbuilt image combiner. We need to combine the images incredible and chall. And under the SUB plane you can see the flag
### Method- 2
We can also do this by importing th cv2open library in python









## FLAG FOUND
`flag{h4ppy_h4ppy_h4ppy_:)}`  

# Image Forensics
## PNG
### c0rrupt3d
#### Process:
Just fixed Magic numbers for the png image as 89 50 4E 47 0D 0A 1A 0A and got the flag.
#### FLAG FOUND:
`vidyutctf{4r3_y4_w1nn1ng_s0n}`

