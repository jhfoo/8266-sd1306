import framebuf

def loadImage(filename):
    with open(filename, 'rb') as f:
        f.readline()
        width, height = [int(v) for v in f.readline().split()]
        data = bytearray(f.read())
    return framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)