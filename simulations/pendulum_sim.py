import numpy as np
import matplotlib.pyplot as plt

G = 9.8 #m/s^2

# x = x0*sin(wt+f0)
def na_pendulum_simulation(
    pivot:np.ndarray, #m
    x0:np.ndarray, #m
    v0:np.ndarray, #m/s
    time:np.ndarray=np.linspace(0, 5, 1001), #s
    m:float = 0.1, #kg
    eq_pos:np.ndarray = np.array([0., 0., 0.])
)->dict:
    """
    calculates position of pendulum, for given time period,\n
    provided the initial conditions.\n
    parameters:
    ---------------------
    #TODO
    """
    results = []
    x = x0
    v = v0
    time_interval = (max(time)-min(time))/len(time)
    gravity = np.array([0, -1*m*G, 0])
    for t in time:
        f = calculate_centripital_force(
            pivot=pivot,
            x=x,
            m=m,
            eq_pos=eq_pos,
            v=v
        )
        x += v*time_interval
        results.append([x[0], x[1], x[2]])
        v += (f + gravity)/m * time_interval
    return {
        "result":np.array(results).T,
        "time": time
    }


def angle_pendulum_sim(
    teta_0:float,
    g:float,
    l:float,
    t:np.ndarray
):
    """
    teta = teta_0 * cos(sqrt(g/l)t)
    """
    return teta_0 * np.cos(np.sqrt(g/l)*t)

def calculate_centripital_force(
    pivot:np.ndarray,
    x:np.ndarray,
    m:float,
    eq_pos:np.ndarray,
    v:np.ndarray
) -> np.ndarray :
        string_length = np.linalg.norm(pivot-eq_pos)
        f_direction = (pivot-x)/string_length
        f_magnitude = np.dot(v,v)/string_length * m + m * G * f_direction[1]
        f = f_direction*f_magnitude
        return f