f = open('file1.txt', 'rt')
lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()  # '\n'
    codes.append(code)

print(codes)

f.close()
