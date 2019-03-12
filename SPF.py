class SPF:
    def __init__(self, LST, host, N):
        self.host = host
        self.LST = LST
        self.Nbar = [host]
        self.N = N
        self.D = {}
        self.p = {}

        for v in self.N:
            if v is not host:
                if self.is_neighbor(v, host):
                    self.D.update({v: self.c(self.host, v)})
                    self.p.update({v: self.host})
                else:
                    self.D.update({v: 99999})

    def c(self, u, v):
        if (u, v) in self.LST.keys():
            return self.LST[(u, v)]
        else:
            return self.LST[(v, u)]

    def is_neighbor(self, u, v):
        if (u, v) in self.LST.keys():
            return True
        elif (v, u) in self.LST.keys():
            return True
        else:
            return False

    def neighbor(self, u):
        neighbor = []
        for v in self.N:
            if self.is_neighbor(u, v):
                neighbor.append(v)
        return neighbor

    def find_minimum(self):
        minimun = ['tmp', 99999]
        for w in self.N:
            if w not in self.Nbar:
                if self.D[w] < minimun[1]:
                    minimun[0] = w
                    minimun[1] = self.D[w]
        return minimun[0]

    def update_D(self, w):
        for v in self.neighbor(w):
            if v not in self.Nbar:
                self.D.update({v: min([self.D[v], self.D[w] + self.c(w, v)])})
                if self.D[w] + self.c(w, v) <= self.D[v]:
                    self.p.update({v: w})

    def is_Nbar_same_as_N(self):
        for u in self.N:
            if u not in self.Nbar:
                return False
        return True


