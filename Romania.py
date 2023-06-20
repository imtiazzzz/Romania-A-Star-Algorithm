import heapq

class priorityQ:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)

class cityNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)

romania = {}

def romadict():
    file = open("romania.txt", 'r')
    for string in file:
        line = string.split(',')
        ct1 = line[0]
        ct2 = line[1]
        dist = int(line[2])
        romania.setdefault(ct1, []).append(cityNode(ct2, dist))
        romania.setdefault(ct2, []).append(cityNode(ct1, dist))

def huristikdict():
    h = {}
    with open("romania_sld.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h

def heuristic(node, values):
    return values[node]

def astar(start, end):
    path = {}
    distance = {}
    q = priorityQ()
    h = huristikdict()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)

            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = current

    printoutput(start, end, path, distance, expandedList)

def printoutput(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
 
    print("\t\t\t\tArad => Bucharest")
    print("\nCities that may be explored \t\t: " + str(expandedlist))
    print("\nPossible cities \t\t: " + str(len(expandedlist)))
    print("\ntraveled by the shortest distance  \t: " + str(finalpath))
    print("\nNumber of cities traveled \t\t\t: " + str(len(finalpath)))
    print("\ntotal distance \t\t\t\t\t\t: " + str(distance[end]))

def main():
    src = "Arad"
    dst = "Bucharest"
    romadict()
    astar(src, dst)

if __name__ == "__main__":
    main()