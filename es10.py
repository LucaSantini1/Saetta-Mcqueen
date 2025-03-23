# Istruzioni
# Definisci la classe Frazione con attributi numeratore e denominatore.
# Implementa il magic method __add__ per sommare due frazioni.
# Implementa il magic method __sub__ per sottrarre due frazioni.
# Implementa il magic method __mul__ per moltiplicare due frazioni.
# Implementa il magic method __str__ per restituire una rappresentazione leggibile della frazione.

class Frazione:
	def __init__(self, numeratore: float, denominatore : float):
		self.numeratore = numeratore
		self.denominatore = denominatore

	@property
	def numeratore(self):
		return self._numeratore

	@property
	def denominatore(self):
		return self._denominatore

	@numeratore.setter
	def numeratore(self, numeratore):
		self._numeratore = numeratore

	@denominatore.setter
	def denominatore(self, den):
		if den == 0.0:
			raise ValueError("Denominatore invalido (inserisci valore positivo)")
		self._denominatore = den

	def __str__(self):
		return f"Frazione ({self.numeratore}, {self.denominatore})"

	def __add__(self, frazione):
		den_new = mcm(self.denominatore, frazione.denominatore)
		num_new = den_new / self.denominatore * self.numeratore + den_new / frazione.denominatore * frazione.numeratore
		return Frazione(num_new, den_new)

	def __sub__(self, frazione):
		return self + Frazione(-frazione.numeratore, frazione.denominatore)

	def __mul__(self, frazione):
		den_new = self.denominatore * frazione.denominatore
		num_new = self.numeratore * frazione.numeratore

		# riduco ai minimi termini
		i = 2
		while i <= min(den_new, num_new):
			print(f"F_TMP ({num_new}, {den_new})")
			while den_new % i == 0 and num_new % i == 0:
				den_new /= i
				num_new /= i
				print(f"divido entrambi per {i} ==> F_TMP ({num_new}, {den_new})")
			i += 1

		return Frazione(num_new, den_new)

	def __truediv__(self, frazione):
		return self * Frazione(frazione.denominatore, frazione.numeratore)

def mcm(a, b):
	ris = max(a, b)
	i = 2

	while ris % min(a, b) != 0:
		ris = max(a, b) * i
		i += 1

	return ris


# Esempio di utilizzo
f1 = Frazione(3.0, 4.0)
f2 = Frazione(2.0, 4.0)

# Addizione
f3 = f1 + f2
print(f3)  # Output: Frazione(5, 4)

# Sottrazione
f4 = f1 - f2
print(f4)  # Output: Frazione(1, 4)

# Moltiplicazione
f5 = f1 * f2
print(f5)  # Output: Frazione(6, 16)

f6 = Frazione(8.0, 4.0) * Frazione(3.0, 12.0)
print(f6)

f7 = Frazione(8.0, 4.0) / Frazione(12.0, 6.0)
print(f7)

# Rappresentazione
print(f1)  # Output: Frazione(3, 4)
