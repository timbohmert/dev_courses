#Fahrenheit to Celcius Function
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp
f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

#Celcius to Fahrenheit Function
def c_to_f(c_temp):
    f_temp = c_temp * 9 / 5 + 32
    return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#Force Function
def get_force(mass, acceleration):
    return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#Energy Function
def get_energy(mass,c = 3 * 10 ** 8):
    return mass * c ** 2
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#Work Function
def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

