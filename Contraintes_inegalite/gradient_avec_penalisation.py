# Imports
import numpy as np

# projection de (x, y) sur Q.
def p_Q(x):

  p = np.zeros(2)
  p[0] = min(x[0], -1./2.)
  p[1] = min(x[1], -1./2.)

  return p

def J(x, y):
  return 2 * x**2 + 2 * y**2 + 3 * x * y

matrix_A = np.array([[4., 3], [3, 4]]) # Matrice associée à J.

def grad_penalise(epsilon, rho, x_0):

  it_max = 100000
  it = 0

  x_last = x_0 
  d = - matrix_A @ x_last - np.array([(2./epsilon) * np.max(x_last[0] + (1./2.), 0) , (2./epsilon) * np.max(x_last[1] + (1./2.), 0) ])
  x_now = x_last + rho * d

  x = [x_0] # liste des itérations x^k.
  err = [] # liste d'erreurs.

  x.append(x_now)
  err.append(np.linalg.norm(x_now - x_last))

  while ((np.linalg.norm(x_now - x_last) > 1e-12) and (it < it_max)):

    it += 1
    x_last = x_now
    d = - matrix_A @ x_last - np.array([(2./epsilon) * np.max(x_last[0] + (1./2.), 0) , (2./epsilon) * np.max(x_last[1] + (1./2.), 0) ])
    x_now = x_last + rho * d
  
    x.append(x_now)
    err.append(np.linalg.norm(x_now - x_last))

  return x, err, it