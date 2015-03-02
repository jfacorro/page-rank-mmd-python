# main.py
class Data():
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.count = 0

    def load(self, file):
        source_file = open(file, 'r')
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

            # if line_count >= 10: break

    def register(self, node):
        if not node in self.nodes:
            self.nodes[node] = self.count
            self.count = self.count + 1

def main(argv):
    data = Data()
    data.load('web.txt')

    print "Nodes " + str(data.count)
    # print "Edges " + str(len(data.edges))
    return 0

def target(*args):
  return main, None

if __name__ == '__main__':
  import sys
  main(sys.argv)
