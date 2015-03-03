# main.py
import math

class Data():
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.count = 0

        self.matrix = {}
        self.beta = 0.8
        self.epsilon = 1e-10
        self.r_old = []
        self.r_new = []

        self.max_iterations = 100
        self.max_edges = None

    def load(self, path):
        source_file = open(path, 'r')
        line_count = 0

        for line in source_file:
            line_count = line_count + 1
            edge = line.split("\t")
            origin = edge[0]
            target = edge[1].strip()
            # print origin + " -> " + target

            self.register(origin)
            self.register(target)

            if not origin in self.edges:
                self.edges[origin]  = []

            self.edges[origin].append(target)

            if self.max_edges is not None and line_count >= self.max_edges:
                break

    def register(self, node):
        if not node in self.nodes:
            self.nodes[node] = self.count
            self.count += 1

    def build_matrix(self):
        out_degree = 1
        for origin in self.edges:
            edges = self.edges[origin]
            out_degree = float(len(edges))
            for target in edges:
                if not target in self.matrix:
                    self.matrix[target] = {}

                self.matrix[target][origin] = self.beta / out_degree

        init = 1 / float(self.count)

        for i in range(self.count):
            self.r_new.append(init)
            self.r_old.append(init)

    def distance(self):
        sum = 0
        diff = 0
        for i in range(self.count):
            diff = self.r_new[i] - self.r_old[i]
            sum += diff * diff

        return math.sqrt(sum)

    def _swap(self):
        tmp = self.r_new
        self.r_new = self.r_old
        self.r_old = tmp

    def _normalize(self, vector):
        sum = 0
        count = len(vector)
        for i in range(count):
            sum += vector[i]
        delta = (1 - sum) / float(count)
        for i in range(len(vector)):
            vector[i] += delta

    def compute_page_rank(self):
        diff = self.epsilon + 1
        iteration = 0
        beta_delta = (1 - self.beta) / float(self.count)
        print "1 - beta / N = " + str(beta_delta)
        while diff > self.epsilon and iteration < self.max_iterations:
            print "Iteration " + str(iteration)
            self._swap()

            for key_i in self.nodes:
                i = self.nodes[key_i]
                self.r_new[i] = beta_delta
                if key_i in self.matrix:
                    for key_j in self.matrix[key_i]:
                        j = self.nodes[key_j]
                        self.r_new[i] += self.matrix[key_i][key_j] * self.r_old[j]

            diff = self.distance()
            iteration += 1

            print "Diff " + str(diff)

        self._normalize(self.r_new)

        return self.r_new

    def get_page_rank(self, node_id):
        i = self.nodes[node_id]
        return self.r_new[i]

def main(argv):
    data = Data()
    data.load('web.txt')
    data.build_matrix()
    data.compute_page_rank()

    print "Nodes " + str(data.count)
    print data.get_page_rank("97")
    print data.get_page_rank("99")
    print data.get_page_rank("101")
    # print data.r_new
    # print data.distance()
    # print data.nodes["99"]
    # print "Edges " + str(len(data.edges))
    return 0

def target(*args):
  return main, None

if __name__ == '__main__':
  import sys
  main(sys.argv)
