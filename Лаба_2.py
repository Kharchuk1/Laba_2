from PIL import Image, ImageDraw

with open('DS4.txt') as f:
    lines = f.readlines()

coor = []
for line in lines:
    formatted_line = line[:-1].split(' ')
    single_coordinate = (int(formatted_line[0]), int(formatted_line[1]))
    coor.append(single_coordinate)

img = Image.new("RGB", (540, 960), (255, 255, 255))
draw = ImageDraw.Draw(img)
draw.point(coor, fill='red')
img.show()
img.save("result.jpg")
