import sys
import io

# Simulate the fix
try:
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    print("Encoding reconfiguration successful.")
except Exception as e:
    print(f"Encoding reconfiguration failed: {e}")

# Test Chinese output
print("测试中文输出")
