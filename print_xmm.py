import lldb
import struct


def print_xmm_value(reg_name, process):
    reg = process.GetThreadAtIndex(0).GetFrameAtIndex(0).FindRegister(reg_name)
    summary = reg.GetSummary()    
    bytes_value = bytes(int(b, 16) for b in summary.replace('0x', '')[1:-1].split(','))
    if len(bytes_value) != 16:
        print(f"Unexpected length of bytes: {len(bytes_value)}")
        return

    # Преобразуем байты в значения double
    doubles = struct.unpack('<2d', bytes_value)
    print(f"{reg_name} eq:", doubles)

# Используем этот скрипт в LLDB
process = lldb.debugger.GetSelectedTarget().GetProcess()
print_xmm_value('xmm0', process)
print_xmm_value('xmm1', process)
print_xmm_value('xmm2', process)
