Scale.default = 'minor'
Clock.bpm = 50

p1 >> loop("nature/01_water_creek", dur=54, amp=0.1)
p2 >> loop("nature/02_wind", dur=54, amp=0.1)

p3 >> play('V  [ X]')

noise_line = [0]
p4 >> noise(noise_line, dur=4, oct=3, amp=linvar([0.5, 0.7], 4))

melody_line = [0, 0, 0, 0, 1, 1, 2, 2]
p5 >> charm(melody_line)
p6 >> glass(melody_line)
p7 >> dirt(melody_line).sometimes("stutter", 3)

sec_melody = [8, 6, 5, 4, 8, 7, 5, 4, 8, 7, 9, 8]
p8 >> sinepad(P[sec_melody] + (1, 2), dur=1/2).sometimes("reverse").sometimes("stutter", 2)

th_melody = [8, 7, 5, 4]
p9 >> sinepad(th_melody, dur=PDur(6,2), oct=5, amp=0.7)

q1 >> rave(noise_line).sometimes("stutter", 3)

q2 >> play('<x-=>(<v>([--]   ))')


