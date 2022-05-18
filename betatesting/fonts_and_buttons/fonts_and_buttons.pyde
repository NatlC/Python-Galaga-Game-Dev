
BTN_HOVER = "#F3DFA2"


def setup():
    size(800,700)


def draw():
    background(0)
    titlefont = createFont("Orbitron.ttf", 40)
    buttonfont = createFont("Orbitron.ttf", 60)
    textFont(titlefont)
    textSize(width/9)
    fill(255)
    text("HYPERSPACE",width/18,height/3)
    
    #play button 
    button_x = 200
    button_y = 350
    button_width = 400
    button_height = 100
    noStroke()
    if (mouseX > button_x and mouseX < button_x + button_width and
            mouseY > button_y and mouseY < button_y + button_height):  # Hovering
        fill(100,150,177)
    else:
        fill(5,70,177)
    rect(button_x, button_y, button_width, button_height, 10)
    
    textFont(buttonfont)
    fill(255)
    text("PLAY", width/2.6,height/1.65)
    
    #controls/tutorial button
    button2_x = 200
    button2_y = 500
    button2_width = 400
    button2_height = 100
    noStroke()
    if (mouseX > button2_x and mouseX < button2_x + button2_width and
            mouseY > button2_y and mouseY < button2_y + button2_height):  # Hovering
        fill(100,150,177)
    else:
        fill(5,70,177)
    rect(button2_x, button2_y, button2_width, button2_height, 10)
    
    textFont(buttonfont)
    fill(255)
    text("CONTROLS", width/3.9,height/1.225)
    
def mousePressed():
    print(mouseX, mouseY)
    
