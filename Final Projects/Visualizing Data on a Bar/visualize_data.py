"""
Image Visualization Project.
This project takes various data from files and provides
an IMAGE DATA BAR using that data having stripes of different
colours from varying from red to green where red represents higher
value and green represents lower value.
The various data files used in this project are listed under:

1. Climate change data: Climate scientists measure temperature again
a "0" point which is a historical global average temperature. Each
year is measured as the "anomaly" from the historical average, so -1.5 C
for a cold year or +1.5 C for a hot year. I scaled the climate data to fit
in the -1.0 .. +1.0 format, but kept the 0 point intact, so when you see
gray years, those were around the long-term average temperature, with red
years above average and blue years below.
This data set is from https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/

2. Child-mortality data: data-child-mortality. txt - global percentage of
children dying before the age of five. The amount of human misery in the left
part of this graph is breathtaking. I trimmed the data to start at 1960 as that's
when there is data for every year. Data from https://ourworldindata.org/child-mortality

3. Illiteracy-data: data-illiteracy.txt - global illiteracy rate.
https://data.unicef.org/topic/education/literacy/

"""

from simpleimage import SimpleImage

GREEN = 127
BLUE = 127

CANVAS_WIDTH = 840
CANVAS_HEIGHT = 200

MAX_RED_VALUE = 255

def draw_stripes(canvas,fraction,startx,stripe_width):

    for y in range(CANVAS_HEIGHT):
        for x in range(startx,startx+stripe_width):
            pixel = canvas.get_pixel(x,y)
            pixel.red= fraction*MAX_RED_VALUE
            pixel.green = GREEN
            pixel.blue = BLUE


def climate_change_image():

    width = 1251
    climate_canvas = SimpleImage.blank(width, CANVAS_HEIGHT)

    climate_data = open("data-climate.txt")
    next(climate_data)

    list = (climate_data.readlines())

    fraction_no = int(list[0])

    stripe_width = width//fraction_no
    list.pop(0)

    for i in range(0, fraction_no):

        fraction = float(list[i])

        startx = i * stripe_width

        draw_stripes(climate_canvas, fraction, startx, stripe_width)

    climate_canvas.show()

def child_mortality_image():
    
    width = 1140
    child_mortality_canvas = SimpleImage.blank(width, CANVAS_HEIGHT)

    child_mortality_data = open("data-child-mortality.txt")
    next(child_mortality_data)

    list = (child_mortality_data.readlines())

    fraction_no = int(list[0])

    stripe_width = width//fraction_no
    list.pop(0)
    
    for i in range(0, fraction_no):
        fraction = float(list[i])
        startx = i * stripe_width
        draw_stripes(child_mortality_canvas, fraction, startx, stripe_width)
        
    child_mortality_canvas.show()

def illiteracy_image():

    width = 930
    illiteracy_canvas = SimpleImage.blank(width, CANVAS_HEIGHT)
    
    illiteracy_data = open("data-illiteracy.txt")
    next(illiteracy_data)

    list = (illiteracy_data.readlines())

    fraction_no = int(list[0])

    stripe_width = width//fraction_no
    list.pop(0)
    
    for i in range(0, fraction_no):
        fraction = float(list[i])
        startx = i * stripe_width
        draw_stripes(illiteracy_canvas, fraction, startx, stripe_width)
        
    illiteracy_canvas.show()


def main():

    climate_change_image()

    child_mortality_image()

    illiteracy_image()

if __name__ == '__main__':
    main()




