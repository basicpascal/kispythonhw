from struct import *

FMT = dict(
    char='>c',
    int8='>b',
    uint8='>B',
    int16='>h',
    uint16='>H',
    int32='>i',
    uint32='>I',
    int64='>q',
    uint64='>Q',
    float='>f',
    double='>d',
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, 'float')
    a2, offs = parse_b(buf, offs)
    a3, offs = parse(buf, offs, 'double')
    a4 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'uint16')
        a4.append(val)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'uint32')
    b2, offs = parse_c(buf, offs)
    b3_size, offs = parse(buf, offs, 'uint16')
    b3_offs, offs = parse(buf, offs, 'uint16')
    b3 = []
    for _ in range(b3_size):
        val, b3_offs = parse(buf, b3_offs, 'char')
        b3.append(val.decode())
    b4, offs = parse(buf, offs, 'uint8')
    b5 = []
    for _ in range(2):
        val, offs = parse(buf, offs, "uint32")
        val_d, _ = parse_d(buf, val)
        b5.append(val_d)
    return dict(B1=b1, B2=b2, B3=''.join(b3), B4=b4, B5=b5), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'uint8')
    c2, offs = parse(buf, offs, 'uint16')
    c3, offs = parse(buf, offs, 'int32')
    c4, offs = parse(buf, offs, 'float')
    c5, offs = parse(buf, offs, 'uint32')
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'int64')
    d2, offs = parse(buf, offs, 'uint64')
    d3 = []
    for _ in range(7):
        val, offs = parse(buf, offs, 'uint16')
        d3.append(val)
    d4, offs = parse(buf, offs, 'uint64')
    return dict(D1=d1, D2=d2, D3=d3, D4=d4), offs


def main(buf):
    return parse_a(buf, 4)[0]


print(main(b'FGL\x1b\xbf\x01W\n=\xb4\xb9I\xe56W?\x08\xd1K>\xf3\xe3\xb7\xdb\xdf\xbe\xf5\x00\x06\x006\x83\x00\x00\x00'
           b'<\x00\x00\x00b?\xebDG\xdf\x06\x17N\xa5\x9dr\xd8w\xe0juitio:\x0b\x96\x18~x\x15\x04\x8cE\xf2% '
           b'\xcb\rZB~2\xb0O\x07\x9d\x13\xcf~A=\xfeDm\xea\xe7\x11\xf1\x85\xb9N\xba\xefu\x87\xc9\xf4\x98\xf4\x17\x87'
           b'\xeb\x1a\x8a\xe3\xfb\xa3\xa6I\xf6-\x97\x96\xb6<*\x1b-\xe8R\xf20C)\xd3\x19\xb9\xb2\xb7'))