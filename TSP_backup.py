from numpy import *
from matplotlib.pyplot import *


def main():
    npts = 10

    xs = random.randn(1, npts)
    ys = random.randn(1, npts)
    xs = xs[0]
    ys = ys[0]
    startIndex = 0
    # startIndex = random.randint(npts - 1)
    startPt = [xs[startIndex], ys[startIndex]]

    dstep = zeros([npts, 1])
    pts = zeros([npts, 2])
    pts[0:] = array([startPt[0], startPt[1]])
    xsLeft = delete(xs, startIndex)
    ysLeft = delete(ys, startIndex)
    ptsLeft = transpose(array([xsLeft, ysLeft]))
    for i in range(npts - 1):

        d = distance(pts[i], ptsLeft)
        index = where(d == amin(d))[0]
        pts[i+1] = ptsLeft[index, :]
        ptsLeft = delete(ptsLeft, index, 0)
        dstep[i] = d[index]
        boll = 0
    boll = 0
    dSum = sum(dstep)
    ptsize = 4
    plot(xs, ys, 'bo-.', markersize=ptsize, linewidth=0.1)
    plot(xs, ys, 'r.', markersize=ptsize)
    plot(startPt[0], startPt[1], 'og', markersize=ptsize * 2)
    plot(pts[:,0], pts[:,1], '-.g')
    print('Each distance: ' + str(dstep))
    print('Total distance: ' + str(dSum))
    show()



def distance(a, b):
    sz = shape(b)
    d = zeros([sz[0], 1])
    for r in range(sz[0]):
        dtemp = 0
        for c in range(sz[1]):
            dtemp = dtemp + (a[c] - b[r, c]) ** 2
        d[r] = sqrt(dtemp)
    return d

if __name__ == '__main__':
    main()