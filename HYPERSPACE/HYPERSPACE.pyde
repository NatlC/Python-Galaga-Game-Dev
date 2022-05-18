keys_pressed = [False for key_code in range(256)]
x, y, player_lives = 400, 550, 1
bullet = []
# x-coordinate, y-coordinate, lives
enemy = [[400, 100, 3], [300, 100, 3], [500, 100, 3]]
# x-coordinate, y-coordinate of enem bullets
enemy_bullet = [[400, 200], [300, 100], [500, 400]]
movement_boolean = True
movement_boolean2 = True
movement_boolean3 = True
bullet_timer_player = True
bullet_timer_enemy = 0
health_bar = 40
page = 0
click_timer = True
timer = 0
count_timer = 0
time = 0
kills = []
combo = 0
shield_timer = 0
shield_cooldown = 0
shield_status = False
recharge_status = False

button_x = 175
button_y = 350
button_width = 450
button_height = 100
button2_x = 175
button2_y = 500
button2_width = 450
button2_height = 100
button3_x = 175
button3_y = 600
button3_width = 450
button3_height = 60


def setup():
    global bullet_sprite, ebullet_sprite, player_sprite
    global enemy1, heart, shieldedSprite
    size(800, 700)
    frameRate(60)
    smooth()
    bullet_sprite = loadImage("Bullet.png")
    ebullet_sprite = loadImage("Enemy Bullet.png")
    player_sprite = loadImage("Plane.png")
    enemy1 = loadImage("Enemy.png")
    heart = loadImage("heart.jpg")
    shieldedSprite = loadImage("Shielded.png")


def draw():
    global timer, page, button_x, button_y
    global button_width, button_height, button2_x
    global button2_y, button2_width, button2_height, button3_x, button3_y
    global button3_width, button3_height, player_lives, bullet_timer_player
    global bullet_timer_enemy, click_timer, count_timer, time, combo, kills
    global shield_timer, shield_cooldown, shield_status, shieldedSprite
    global recharge_status
    rectMode(CORNER)
    noStroke()
    textAlign(LEFT)

    if page == 0:
        cursor()
        reset()
        titlefont = createFont("Orbitron.ttf", 40)
        buttonfont = createFont("Orbitron.ttf", 60)
        background(0)
        textFont(titlefont)
        textSize(width/9)
        fill(0, 255, 0)
        text("HYPERSPACE", width/18, height/3)

        # play button
        if (mouseX > button_x and mouseX < button_x + button_width and
            mouseY > button_y and mouseY < button_y + button_height and
                mousePressed):
            page = 1
        elif (mouseX > button_x and mouseX < button_x + button_width and
                mouseY > button_y and mouseY < button_y + button_height):
            fill(100, 150, 177)
        else:
            fill(5, 70, 177)

        rect(button_x, button_y, button_width, button_height, 10)
        textFont(buttonfont)
        fill(255)
        text("PLAY", width/2.6, height/1.65)

        # controls/tutorial button
        if (mouseX > button2_x and mouseX < button2_x + button2_width and
                mouseY > button2_y and mouseY < button2_y + button2_height and
                mousePressed):
            page = 2
        elif (mouseX > button2_x and mouseX < button2_x + button2_width and
                mouseY > button2_y and mouseY < button2_y + button2_height):
            fill(100, 150, 177)
        else:
            fill(5, 70, 177)

        rect(button2_x, button2_y, button2_width, button2_height, 10)
        textFont(buttonfont)
        fill(255)
        text("CONTROLS", width/3.9, height/1.225)

    if page == 1:  # Game
        noCursor()
        game()
        framecount()
        death()
        times()
        live()

    if page == 2:  # Controls
        cursor()
        background(0)
        titlefont2 = createFont("Orbitron.ttf", 40)
        buttonfont2 = createFont("Orbitron.ttf", 50)
        textfont = createFont("Orbitron.ttf", 50)
        descriptionfont = createFont("Orbitron.ttf", 25)
        textFont(titlefont2)
        textSize(width/9)
        fill(255, 0, 0)
        text("CONTROLS", width/7, height/6)
        textFont(textfont)
        text("W A S D - Movement", width/16, height/3.5)
        text("LMB - To Fire Cannons", width/16, height/2.5)
        text("Click P to pause the game", width/16, height/1.9)
        text("L SHIFT - To Open Sheild", width/16, height/1.4)
        textFont(descriptionfont)
        text("Click LMB to unpause", width/16, height/1.7)
        text("Shields last 5 seconds and can absorb 5 hits",
             width/16, height/1.3)
        text("before turning off. Recharging takes 30 seconds",
             width/16, height/1.22)

        if (mouseX > button3_x and mouseX < button3_x + button3_width and
            mouseY > button3_y and mouseY < button3_y + button3_height and
                mousePressed):
            page = 0
        elif (mouseX > button3_x and mouseX < button3_x + button3_width and
                mouseY > button3_y and mouseY < button3_y + button3_height):
            fill(100, 150, 177)
        else:
            fill(5, 70, 177)

        rect(button3_x, button3_y, button3_width, button3_height, 10)
        textFont(buttonfont2)
        fill(255)
        text("BACK TO MENU", width/4.4, height/1.08)

    if page == 3:  # Player Death
        cursor()
        background(0)
        titlefont3 = createFont("Orbitron.ttf", 70)
        buttonfont3 = createFont("Orbitron.ttf", 50)
        statsfont = createFont("Orbitron.ttf", 70)
        noStroke()
        textFont(titlefont3)
        fill(255, 0, 0)
        text("<< GAME OVER >>", width/11, height/5)
        textFont(statsfont)
        text('TIME: {}'.format(time), width/16, height/3)
        textFont(statsfont)
        text('KILLS: {}'.format(kills), width/16, height/2.2)
        textFont(statsfont)
        text('LIVES LEFT: 0', width/16, height/1.7)
        textFont(statsfont)
        text('END COMBO: {}'.format(combo), width/16, height/1.35)

        if (mouseX > button3_x and mouseX < button3_x + button3_width and
            mouseY > button3_y and mouseY < button3_y + button3_height and
                mousePressed):
            page = 0
        elif (mouseX > button3_x and mouseX < button3_x + button3_width and
                mouseY > button3_y and mouseY < button3_y + button3_height):
            fill(100, 150, 177)
        else:
            fill(5, 70, 177)

        rect(button3_x, button3_y, button3_width, button3_height, 10)
        textFont(buttonfont3)
        fill(255)
        text("BACK TO MENU", width/4.4, height/1.08)

    if page == 4:
        cursor()
        background(0)
        titlefont4 = createFont("Orbitron.ttf", 70)
        buttonfont4 = createFont("Orbitron.ttf", 50)
        statsfont2 = createFont("Orbitron.ttf", 70)
        noStroke()
        textFont(titlefont4)
        fill(255, 223, 0)
        text("<< VICTORY >>", width/5.5, height/5)
        textFont(statsfont2)
        fill(255)
        text('TIME: {}'.format(time), width/16, height/3)
        textFont(statsfont2)
        text('KILLS: {}'.format(kills), width/16, height/2.2)
        textFont(statsfont2)
        text('LIVES LEFT: {}'.format(player_lives), width/16, height/1.7)
        textFont(statsfont2)
        text('END COMBO: {}'.format(combo), width/16, height/1.35)
        if (mouseX > button3_x and mouseX < button3_x + button3_width and
                mouseY > button3_y and mouseY < button3_y +
                button3_height and mousePressed):
            page = 0
        elif (mouseX > button3_x and mouseX < button3_x + button3_width and
                mouseY > button3_y and mouseY < button3_y + button3_height):
            fill(100, 150, 177)
        else:
            fill(5, 70, 177)

        rect(button3_x, button3_y, button3_width, button3_height, 10)
        textFont(buttonfont4)
        fill(255)
        text("BACK TO MENU", width/4.4, height/1.08)


def game():
    global movement_boolean, movement_boolean2
    global movement_boolean3, pause, timer, x, y
    global bullet, enemy, enemy_bullet, bullet_timer_player, health_bar, page
    global bullet_timer_enemy, click_timer, count_timer, time, kills, combo
    global shield_timer, shield_cooldown, shield_status
    global shieldedSprite, recharge_status

    background(0)
    stroke(1)
    timer += 1

    # bullets
    # Not being able to spam bullets
    if not click_timer:
        count_timer += 1
        if count_timer >= 25:
            click_timer = True

    # time it takes to get more bullets
    if mousePressed and click_timer:
        if timer > 20:
            bullet.append([x, y])

    # times bullets with mousePressed
    if timer > 20.5:
        timer = 0

    # make bullets and track where the bullet is corresponding to enemy planes
    try:
        for i in range(len(bullet)):
            fill(0, 0, 255)
            image(bullet_sprite, bullet[i][0], bullet[i][1] - 25)
            bullet[i][1] -= 15
            for k in range(len(bullet)):
                try:
                    # enemy 1
                    if (enemy[0][0] - 25 <= bullet[k][0] <=
                        enemy[0][0] + 25 and
                            bullet[k][1] >= enemy[0][1] - 25 and
                            bullet[k][1] <= enemy[0][1] + 25):
                        del bullet[k]
                        count_timer = 25
                        fill(255, 0, 0)
                        u = enemy[0][2] - 1
                        del enemy[0][2]
                        enemy[0].append(u)
                        if enemy[0][2] == 0:
                            kills.append(1)
                            del enemy[0]

                    # enemy 2
                    if (enemy[1][0] - 25 <= bullet[k][0] <=
                        enemy[1][0] + 25 and
                            bullet[k][1] >= enemy[1][1] - 25 and
                            bullet[k][1] <= enemy[1][1] + 25):
                        fill(255, 0, 0)
                        del bullet[k]
                        count_timer = 25
                        d = enemy[1][2] - 1
                        del enemy[1][2]
                        enemy[1].append(d)
                        if enemy[1][2] == 0:
                            kills.append(1)
                            del enemy[1]

                    # enemy 3
                    if (enemy[2][0] - 25 <= bullet[k][0] <=
                        enemy[2][0] + 25 and
                            bullet[k][1] >= enemy[2][1] - 25 and
                            bullet[k][1] <= enemy[2][1] + 25):
                        del bullet[k]
                        count_timer = 25
                        fill(255, 0, 0)
                        e = enemy[2][2] - 1
                        del enemy[2][2]
                        enemy[2].append(e)
                        if enemy[2][2] == 0:
                            kills.append(1)
                            del enemy[2]
                except:
                    pass
    except:
        pass

    try:
        # draws enemies
        fill(0, 255, 0)
        image(enemy1, enemy[0][0], enemy[0][1])
        image(enemy1, enemy[1][0], enemy[1][1])
        image(enemy1, enemy[2][0], enemy[2][1])
    except:
        pass

    # delete bullets that are off the screen
    try:
        for h in range(len(bullet)):
            if bullet[len(bullet) - 1][1] < 0:
                del bullet[h]
                bullet_timer_player = True
    except:
        pass

    # main player
    imageMode(CENTER)
    rectMode(CENTER)
    fill(255, 0, 0)
    image(player_sprite, x, y)

    # movement
    if keys_pressed[87]:  # forward
        y -= 6
        if y <= 25:
            y = 25
    if keys_pressed[83]:  # back
        y += 6
        if y >= 675:
            y = 675
    if keys_pressed[65]:  # left
        x -= 6
        if x <= 25:
            x = 25
    if keys_pressed[68]:  # right
        x += 6
        if x >= 775:
            x = 775
    # Shields
    if recharge_status:
        shield_cooldown += 1
        rect(400, 0, shield_cooldown, 10)

    if shield_cooldown == 850:
        recharge_status = False

    if shield_cooldown >= 850:
        shield_status = False
        shield_cooldown = 0

    if keys_pressed[16] and not shield_status:
        if shield_cooldown == 0:
            shield_status = True

    if shield_timer >= 59 or shieldCapacity <= 0:
        shield_status = False
        shield_timer = 0
        recharge_status = True
        image(shieldedSprite, 1000, 1000)

    if shield_status:
        shield_timer += 1
        image(shieldedSprite, x, y - 5)



    try:
        # enemy 1 health_bar
        fill(0, 255,  0)
        rectMode(CORNER)
        if 40 / 3 * enemy[0][2] / 40 * 100 <= 66:
            health_bar = 40 / 3 * enemy[0][2]
        elif 40 / 3 * enemy[0][2] / 40 * 100 <= 33:
            health_bar = 40 / 3 * enemy[0][2]

        rect(enemy[0][0] - 21, enemy[0][1] - 35, health_bar, 5)
    except:
        pass

    try:
        # enemy 2 health_bar
        if 40 / 3 * enemy[1][2] / 40 * 100 <= 66:
            health_bar = 40 / 3 * enemy[1][2]
        elif 40 / 3 * 1 / 40 * 100 <= 33:
            health_bar = 40 / 3 * enemy[1][2]

        rect(enemy[1][0] - 21, enemy[1][1] - 35, health_bar, 5)
    except:
        pass

    try:
        # enemy 3 health_bar
        if 40 / 3 * enemy[2][2] / 40 * 100 <= 66:
            health_bar = 40 / 3 * enemy[2][2]
        elif 40 / 3 * 1 / 40 * 100 <= 33:
            health_bar = 40 / 3 * enemy[2][2]

        rect(enemy[2][0] - 21, enemy[2][1] - 35, health_bar, 5)
    except:
        pass

    # enemy desinated movement
    try:
        # Movement enemy 1
        if movement_boolean:
            enemy[0][0] += 4
            enemy[0][1] += 4
            if enemy[0][0] > 750:
                movement_boolean = False

        if not movement_boolean:
            enemy[0][0] -= 4
            enemy[0][1] += 4
            if enemy[0][0] < 50:
                movement_boolean = True

        if enemy[0][1] >= 700:
            enemy[0][1] = - 25
    except:
        pass

    try:
        # Movement enemy 2
        if movement_boolean2:
            enemy[1][0] += 4
            enemy[1][1] += 4
            if enemy[1][0] > 750:
                movement_boolean2 = False
        if not movement_boolean2:
            enemy[1][0] -= 4
            enemy[1][1] += 4
            if enemy[1][0] < 50:
                movement_boolean2 = True

        if enemy[1][1] >= 700:
            enemy[1][1] = - 25
    except:
        pass

    try:
        # movement enemy 3
        if movement_boolean3:
            enemy[2][0] += 4
            enemy[2][1] += 4
            if enemy[2][0] > 750:
                movement_boolean3 = False

        if not movement_boolean3:
            enemy[2][0] -= 4
            enemy[2][1] += 4
            if enemy[2][0] < 50:
                movement_boolean3 = True

        if enemy[2][1] >= 700:
            enemy[2][1] = - 25
    except:
        pass

    # bullets of enemies
    try:
        # enemy 1
        bullet_timer_enemy += 1
        if bullet_timer_enemy % 60 == 0:
            del enemy_bullet[0][0]
            del enemy_bullet[0][0]
            enemy_bullet[0].append(enemy[0][0])
            enemy_bullet[0].append(enemy[0][1])

        fill(128, 0, 128)
        rectMode(CENTER)
        image(ebullet_sprite, enemy_bullet[0][0], enemy_bullet[0][1])
        enemy_bullet[0][1] += 15
    except:
        pass

    try:
        # enemy 2
        if bullet_timer_enemy % 65 == 0:
            del enemy_bullet[1][0]
            del enemy_bullet[1][0]
            enemy_bullet[1].append(enemy[1][0])
            enemy_bullet[1].append(enemy[1][1])

        fill(128, 0, 128)
        rectMode(CENTER)
        image(ebullet_sprite, enemy_bullet[1][0], enemy_bullet[1][1])
        enemy_bullet[1][1] += 15

    except:
        pass

    try:
        # enemy 3
        if bullet_timer_enemy % 60 == 0:
            del enemy_bullet[2][0]
            del enemy_bullet[2][0]
            enemy_bullet[2].append(enemy[2][0])
            enemy_bullet[2].append(enemy[2][1])

        fill(128, 0, 128)
        rectMode(CENTER)
        image(ebullet_sprite, enemy_bullet[2][0], enemy_bullet[2][1])
        enemy_bullet[2][1] += 15

    except:
        pass

    # Time of duration of enemies fire rate
    if bullet_timer_enemy >= 70:
        bullet_timer_enemy = 0

    # When all planes are dead
    if enemy == []:
        page = 4


# when player dies
def death():
    global x, y, enemy, player_lives, page, shield_status
    try:
        if (enemy[0][0] >= x - 45 and enemy[0][0] <= x + 45 and
                enemy[0][1] >= y - 45 and enemy[0][1] <= y + 45):
            page = 3

        if (enemy[1][0] >= x - 45 and enemy[1][0] <= x + 45 and
                enemy[1][1] >= y - 45 and enemy[1][1] <= y + 45):
            page = 3

        if (enemy[2][0] >= x - 45 and enemy[2][0] <= x + 45 and
                enemy[2][1] >= y - 45 and enemy[2][1] <= y + 45):
            page = 3
    except:
        pass

    # enemy bullet contact point with the plane
    try:
        if (x - 35 <= enemy_bullet[0][0] - 10 and x + 35 >=
                enemy_bullet[0][0] + 10 and
                y - 35 <= enemy_bullet[0][1] - 10 and y + 35 >=
                enemy_bullet[0][1] + 10):
            page = 3

        if (x - 35 <= enemy_bullet[1][0] - 10 and x + 35 >=
                enemy_bullet[1][0] + 10 and
                y - 35 <= enemy_bullet[1][1] - 10 and y + 35 >=
                enemy_bullet[1][1] + 10):
            page = 3

        if (x - 35 <= enemy_bullet[2][0] - 10 and x + 35 >=
                enemy_bullet[2][0] + 10 and
                y - 35 <= enemy_bullet[2][1] - 10 and y + 35 >=
                enemy_bullet[2][1] + 10):
            page = 3

    except:
        pass

    # enemy contact point with the shield
    try:
        if (x - 125 <= enemy_bullet[0][0] - 10 and x + 125 >=
            enemy_bullet[0][0] + 10 and
                y - 125 <= enemy_bullet[0][1] - 10 and y + 125 >=
                enemy_bullet[0][1] + 10):
            if shield_status:
                del enemy_bullet[0][0]
                del enemy_bullet[0][0]
                enemy_bullet[0].append(-10)
                enemy_bullet[0].append(0)

        if (x - 125 <= enemy_bullet[1][0] - 10 and x + 125 >=
            enemy_bullet[1][0] + 10 and
                y - 125 <= enemy_bullet[1][1] - 10 and y + 125 >=
                enemy_bullet[1][1] + 10):
            if shield_status:
                del enemy_bullet[1][0]
                del enemy_bullet[1][0]
                enemy_bullet[1].append(-10)
                enemy_bullet[1].append(0)

        if (x - 125 <= enemy_bullet[2][0] - 10 and x + 125 >=
            enemy_bullet[2][0] + 10 and
                y - 125 <= enemy_bullet[2][1] - 10 and y + 125 >=
                enemy_bullet[2][1] + 10):
            if shield_status:
                del enemy_bullet[2][0]
                del enemy_bullet[2][0]
                enemy_bullet[2].append(-10)
                enemy_bullet[2].append(0)
    except:
        pass


# Resets all variables when the game is played again
def reset():
    global x, y, player_lives, enemy, enemy_bullet
    global bullet_timer_enemy, bulletPlayerTimer
    global health_bar, page, count_timer, time, kills, combo, bullet
    global shield_timer, shield_cooldown, shield_status
    global shieldCapacity, recharge_status
    keys_pressed = [False for key_code in range(256)]
    x, y, player_lives = 400, 550, 1
    enemy = [[400, 100, 3], [300, 100, 3], [500, 100, 3]]
    enemy_bullet = [[400, 200], [300, 100], [500, 400]]
    z = True
    bullet_timer_player = True
    click_timer = True
    bullet_timer_enemy = 0
    health_bar = 40
    count_timer = 0
    time = 0
    combo = 0
    kills = []
    bullet = []
    shield_timer = 0
    shield_cooldown = 0
    shield_status = False
    shieldCapacity = 2
    recharge_status = False


# Shows fps in the top left corner
def framecount():
    global enemy
    textSize(12)
    textAlign(LEFT, TOP)

    if int(frameRate // 1) <= 30:
        fill(255, 0, 0)
    else:
        fill(0, 255, 0)

    text('fps:{}'.format(int(frameRate // 1)), 2, 0)


# shows how many lives you have
def live():
    global heart
    noStroke()
    textSize(50)
    textAlign(BOTTOM, LEFT)
    fill(0, 255, 0)
    text('Live', 120, 690)
    image(heart, 60, 640)
    textAlign(BOTTOM, RIGHT)
    textSize(15)
    fill(0, 255, 255)
    text("Click 'p' to pause", 650, 690)


# shows the time and increases it
def times():
    global time
    time += 100
    fill(255, 223, 0)
    textAlign(TOP, RIGHT)
    textSize(20)
    text('TIME: {}'.format(time), 600, 20)


def keyPressed():
    global keys_pressed
    keys_pressed[keyCode] = True

    # pause button
    if keys_pressed[80]:  # p
        rectMode(CENTER)
        fill(0, 0, 0, 210)
        rect(400, 350, 1000, 1000)
        textAlign(CENTER)
        textSize(100)
        fill(0, 255, 0)
        text('Pause', 400, 350)
        textAlign(CENTER, TOP)
        textSize(50)
        fill(255)
        text('Click LMB to continue', 400, 400)
        noLoop()


def keyReleased():
    global keys_pressed
    keys_pressed[keyCode] = False


# stops spamming mousebutton to fire
def mousePressed():
    loop()
    global bullet, click_timer
    if click_timer:
        bullet.append([x, y])
        click_timer = False


def mouseReleased():
    global click_timer, count_timer
    click_timer = False
    count_timer = 0
