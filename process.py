import numpy as np
import matplotlib.pyplot as plt
import pylab

def plot_output():
  f = open('build/output.txt')
  #time_stamp px_state  py_state  v_state yaw_angle_state yaw_rate_state  sensor_type NIS px_measured py_measured px_ground_truth py_ground_truth vx_ground_truth vy_ground_truth
  data = []
  counter = 0
  for line in f:
    counter += 1
    if counter > 1:
      words = line.split('\t')
      row = []
      for word in words:
        row.append(word)
      data.append(row)

  m = np.matrix(data)
  t = m[:,0]
  px = m[:,1]
  py = m[:,2]
  v = m[:,3]
  yaw = m[:,4]
  yaw_rate = m[:,5]
  sensor_type = m[:,6]
  NIS = m[:,7]
  measx = m[:,8]
  measy = m[:,9]
  gtpx = m[:,10]
  gtpy = m[:,11]
  gtvx = m[:,8]
  gtvy = m[:,9]
  #t = m[:,10]
  #t = (t-t[0])*1e-6
  #t = range(px.shape[0])
 
  plt.subplot(2,2,1)
  plt.plot(t, px)
  plt.plot(t, gtpx)
  plt.plot(t, measx)
  plt.subplot(2,2,2)
  plt.plot(t, py)
  plt.plot(t, gtpy)
  plt.plot(t, measy)
  plt.subplot(2,2,3)
  plt.plot(t, yaw_rate)
  plt.subplot(2,2,4)
  plt.plot(px, py)
  plt.plot(gtpx, gtpy)
  plt.show()

# def plot_in():
#L(for laser) meas_px meas_py timestamp gt_px gt_py gt_vx gt_vy
#R(for radar) meas_rho meas_phi meas_rho_dot timestamp gt_px gt_py gt_vx gt_vy

  # f = open('./data/obj_pose-laser-radar-synthetic-input.txt', 'r')
  # data = []
  # for line in f:
  #   words = line.split(line)
  #   row = []
  #   for word in words:


if __name__ == '__main__':
  plot_output()
