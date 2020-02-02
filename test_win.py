import simulate

sim = simulate.QuantumSimulation()

def test_measure(t1, t2, p):

	n = 0

	for i in range(100):

		sim.measure(t1, t2, p)

		n += 1 if sim.did_win[1] else 0

	print(n)
