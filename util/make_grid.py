import random
import json


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.nNeighbors = []
        self.sNeighbors = []
        self.eNeighbors = []
        self.wNeighbors = []


class BigMap:
    def __init__(self, W, H, minSize, maxSize, minRooms):
        self.W = W
        self.H = H
        self.minSize = minSize
        self.maxSize = maxSize
        self.RoomList = [Rectangle(0, 0, self.W, self.H)]
        self.minRooms = minRooms
        self.worldArray = [[' ' for i in range(self.W)] for j in range(self.H)]

    def buildWorld(self):
        for index, rect in enumerate(self.RoomList):
            shouldSplit = bool(random.getrandbits(1))
            if rect.w <= 2*self.minSize or rect.h <= 2*self.minSize:
                continue
            if rect.w >= self.maxSize and rect.h >= self.maxSize or shouldSplit == 1:
                # split the rect into four rects
                # determine the split locations vertically and horizontally
                hSplit = self.minSize + \
                    random.randrange(0, rect.h - (2*self.minSize))
                wSplit = self.minSize + \
                    random.randrange(0, rect.w - (2*self.minSize))
                # add the rects to the end of the list
                rect1 = Rectangle(rect.x, rect.y, wSplit, hSplit)
                self.RoomList.append(rect1)
                rect2 = Rectangle(rect.x + wSplit, rect.y,
                                  rect.w - wSplit, hSplit)
                self.RoomList.append(rect2)

                rect3 = Rectangle(rect.x, rect.y + hSplit,
                                  wSplit, rect.h-hSplit)
                self.RoomList.append(rect3)
                rect4 = Rectangle(rect.x + wSplit, rect.y + hSplit,
                                  rect.w - wSplit, rect.h-hSplit)
                self.RoomList.append(rect4)
                # update neighbors
                rect1.eNeighbors = rect2
                rect1.sNeighbors = rect3
                rect2.wNeighbors = rect1
                rect2.sNeighbors = rect4
                rect3.nNeighbors = rect1
                rect3.eNeighbors = rect4
                rect4.wNeighbors = rect3
                rect4.nNeighbors = rect2
                # remove original rect from the list
                del self.RoomList[index]
        if len(self.RoomList) < self.minRooms:
            self.buildWorld()

        for room in self.RoomList:
            for i in range(room.x, room.x + room.w):
                if room.nNeighbors and i <= (room.nNeighbors.x + room.nNeighbors.w):
                    self.worldArray[i][room.y] = 'z'
                else:
                    self.worldArray[i][room.y] = '#'
                if room.sNeighbors and i <= (room.sNeighbors.x + room.sNeighbors.w):
                    self.worldArray[i][room.y+room.h - 1] = 'z'
                else:
                    self.worldArray[i][room.y+room.h - 1] = "#"
            for j in range(room.y, room.y + room.h):
                if room.wNeighbors and j <= (room.wNeighbors.x + room.wNeighbors.w):
                    self.worldArray[room.x][j] = 'z'
                else:
                    self.worldArray[room.x][j] = "#"
                if room.eNeighbors and j <= (room.eNeighbors.x + room.eNeighbors.w):
                    self.worldArray[room.x + room.w - 1][j] = 'z'
                else:
                    self.worldArray[room.x + room.w - 1][j] = "#"

        # return self.RoomList

        print('\n'.join([''.join(['{:2}'.format(item)
                                  for item in row])for row in self.worldArray]))
        print(len(self.RoomList))


map = BigMap(64, 64, 5, 10, 30)

map.buildWorld()
