# main.py

class Data():
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.matrix = {}
        self.beta = 0.8
        self.epsilon = 0.00000000001
        self.count = 0

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

            if line_count >= 10000000: break

    def register(self, node):
        if not node in self.nodes:
            self.nodes[node] = self.count
            self.count = self.count + 1

    def build_matrix(self):
        for origin in self.nodes:
            edges = self.edges[origin] if origin in self.edges else None
            if not edges is None:
                count = len(edges)
                for target in edges:
                    if not origin in self.matrix:
                        self.matrix[origin] = {}

                    self.matrix[origin][target] = 1 / count

def main(argv):
    data = Data()
    data.load('web.txt')
    data.build_matrix()

    print "Nodes " + str(data.count)
    # print data.matrix
    # print data.nodes["99"]
    # print "Edges " + str(len(data.edges))
    return 0

def target(*args):
  return main, None

if __name__ == '__main__':
  import sys
  main(sys.argv)
