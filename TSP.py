from numpy import *
from matplotlib.pyplot import *


def main():
    npts = 200

    xs = random.rand(1, npts)
    ys = random.rand(1, npts)
    xs = xs[0]
    ys = ys[0]
    dSum = zeros([npts, 1])
    for p in range(npts):
        startIndex = p
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
        dSum[p] = sum(dstep)

    bestStartInedx = where(dSum == amin(dSum))[0]
    fett = NN(xs, ys, npts, bestStartInedx)
    bestPts = fett[0]
    bestD = fett[1]

    # Post-processing
    ptsize = 4
    plot(xs, ys, 'bo-.', markersize=ptsize, linewidth=0.1)
    plot(xs, ys, 'r.', markersize=ptsize)
    plot(bestPts[0][0], bestPts[0][1], 'og', markersize=ptsize * 2)
    plot(bestPts[:,0], bestPts[:,1], '-.g')
    print('Each distance: ' + str(bestD))
    print('Total distance: ' + str(sum(bestD)))
    show()



def distance(a, b):                 # Euclidian distance
    sz = shape(b)
    d = zeros([sz[0], 1])
    for r in range(sz[0]):
        dtemp = 0
        for c in range(sz[1]):
            dtemp = dtemp + (a[c] - b[r, c]) ** 2
        d[r] = sqrt(dtemp)
    return d


def NN(xs, ys, npts, startIndex):       # Nearest neighbour

    startPt = [xs[startIndex], ys[startIndex]]


    dstep = zeros([npts, 1])
    pts = zeros([npts, 2])
    pts[0:] = transpose(array([startPt[0], startPt[1]]))
    xsLeft = delete(xs, startIndex)
    ysLeft = delete(ys, startIndex)
    ptsLeft = transpose(array([xsLeft, ysLeft]))
    for i in range(npts - 1):
        d = distance(pts[i], ptsLeft)
        index = where(d == amin(d))[0]
        pts[i+1] = ptsLeft[index, :]
        ptsLeft = delete(ptsLeft, index, 0)
        dstep[i] = d[index]
    return pts, dstep



if __name__ == '__main__':
    main()