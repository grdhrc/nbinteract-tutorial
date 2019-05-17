import matplotlib.pyplot as plt

# in Kbps
file = 10 * 10**6
upload = 20 * 1000
download = 1000

def cs1(n):
    return max(n*file/upload, file/download)

def p2p1(n, u):
    return max(file/upload, file/download, n*file/(upload + sum(u)))

if __name__ == '__main__':
    peers = [10, 100, 200, 300, 400, 500, 600, 700, 800, 1000]
    u = [100, 200, 250, 300, 400, 500, 600, 700, 800, 1000]
    plotcs = [cs1(n) for n in peers]
    plotp2p = [p2p1(peers[i], [u[i]] * peers[i]) for i in range(len(peers))]
    plt.plot(peers, plotcs, 'bo')
    plt.plot(peers, plotcs, 'b', label='Client Server Architecture')
    plt.plot(peers, plotp2p, 'ro')
    plt.plot(peers, plotp2p, 'r', label='Peer To peer architecture')
    plt.legend(loc='upper-left')
    plt.title('Minimum Distribution Time for Client-Server vs Peer-to-Peer')
    plt.xlabel('Number of Peers')
    plt.ylabel('Minimum Distribution Time (s)')
    plt.show()
