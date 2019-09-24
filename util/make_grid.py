import random


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


class BigMap:
    def __init__(self, W, H, minSize, maxSize, minRooms):
        self.W = W
        self.H = H
        self.minSize = minSize
        self.maxSize = maxSize
        self.RoomList = [Rectangle(0, 0, self.W, self.H)]
        self.minRooms = minRooms

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
                # remove original rect from the list
                del self.RoomList[index]
        if len(self.RoomList) < self.minRooms:
            self.buildWorld()
        count = 0
        for room in self.RoomList:
            count += 1
            print(f"{count} x: {room.x}, y: {room.y}, w: {room.w}, h: {room.h}")


map = BigMap(1024, 1024, 10, 16, 500)

map.buildWorld()
