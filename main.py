
def maqSlightRight():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 30)

def maqSlightLeft():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 30)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)

##########################
def on_forever():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)==0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)==0:
      #  basic.show_string("S")
      maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 200)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)==1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)==0:
      #  basic.show_string("R")
      maqSlightRight()
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)==0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)==1:
       # basic.show_string("L")
      maqSlightLeft()
basic.forever(on_forever)

#止まる
def maqStop():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)

def on_button_pressed_a():
    maqStop()
input.on_button_pressed(Button.A, on_button_pressed_a)