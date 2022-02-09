def compressBox(boxes):
    for box in boxes:
        print(boxes)


def compressBoxesTwice(boxes,boxes2): #O(N+M)

    compressBox(boxes) #O(N)
    
    compressBox(boxes2) #O(M)
    

compressBoxesTwice(['box1','box2','box3'],['Box1','Box2','Box3','Box4'])