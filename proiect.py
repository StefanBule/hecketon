import turtle
import random

# Setări inițiale
screen = turtle.Screen()
screen.title("Joc cu Mașinuțe")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Lățimea unei linii de drum
lane_width = 600 // 6

# Crearea mașinuței jucător
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, -250)

# Crearea listei pentru mașini inamice
enemies = []

# Variabilă pentru puncte
score = 0

# Crearea turtle pentru afișarea punctelor
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)
score_turtle.color("white")
score_turtle.penup()
score_turtle.goto(0, 260)

# Funcție pentru a actualiza punctajul pe ecran
def update_score():
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Funcție pentru a crea mașini inamice
def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape("square")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    lane = random.randint(0, 5)  # Alege una din cele 6 linii de drum
    x = -250 + lane * lane_width + lane_width // 2
    y = random.randint(200, 500)
    enemy.goto(x, y)
    enemies.append(enemy)

# Funcție pentru a distruge o mașină inamică
def destroy_enemy(enemy):
    enemy.hideturtle()
    enemies.remove(enemy)

# Verificarea coliziunii între jucător și mașini inamice
def check_collision():
    for enemy in enemies:
        if enemy.distance(player) < 20:
            return True
    return False

# Crearea funcțiilor de mișcare pentru jucător
def move_left():
    current_lane = (player.xcor() + 250) // lane_width
    new_lane = current_lane - 1
    if new_lane >= 0:
        x = -250 + new_lane * lane_width + lane_width // 2
        player.setx(x)

def move_right():
    current_lane = (player.xcor() + 250) // lane_width
    new_lane = current_lane + 1
    if new_lane < 6:
        x = -250 + new_lane * lane_width + lane_width // 2
        player.setx(x)



# Asocierea funcțiilor de mișcare la tastele săgeată
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")


# Bucla principală a jocului
while True:
    screen.update()

    # Crearea unei mașini inamice noi la fiecare 50 de cadre (mai rar)
    if random.randint(1, 150) == 1:
        create_enemy()

    # Verificarea coliziunii
    if check_collision():
        print("Game Over")
        break

    # Mișcarea mașinilor inamice existente
    for enemy in enemies:
        y = enemy.ycor()
        y -= 0.4
        enemy.sety(y)

        # Verificarea ieșirii mașinilor inamice din ecran
        if enemy.ycor() < -280:
            destroy_enemy(enemy)
            score += 1
            update_score()

turtle.done()
