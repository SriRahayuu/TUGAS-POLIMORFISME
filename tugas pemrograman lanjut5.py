class FakultasTeknik:
	def __init__(self, Univ, Fak, thnajr):
		self.universitas = Univ
		self.fakultas = Fak
		self.tahunAjar = thnajr

	def CetakData(self):

		print("universitas\t: ",self.universitas)
		print("fakultas\t: ",self.fakultas)
		print("tahun ajar\t: ",self.tahunAjar)

class TeknikKomputer(FakultasTeknik):
	def __init__(self, Univ, Fak, thnajr, JA):
		self.jumlahAngkatan = JA
		FakultasTeknik.__init__(self, Univ, Fak, thnajr)

	def CetakData(self):
		print(100*"=")
		print("teknik komputer")
		print("Univ: ", self.universitas)
		print("Fak: ",self.fakultas)
		print("TA: ",self.tahunAjar)
		print("Jumlah Angkatan di prodi Teknik Komputer adalah" ,self.jumlahAngkatan)

class TeknikMekatronika(FakultasTeknik):
	def __init__(self, Univ, Fak, thnajr, JA):
		self.jumlahAngkatan = JA
		FakultasTeknik. __init__(self, Univ, Fak, thnajr)
	def CetakData(self):
		print("vokasi mekatronika")
		print("Univ\t:",self.universitas)
		print("Fak\t:",self.fakultas)
		print("JumlahAngkatan di prodi Teknik Komputer adalah",self.jumlahAngkatan)
		print(100*"=")

class PTIK(FakultasTeknik):
	def __init__(self, Univ, Fak, thnajr, JA, jur):
		self.jumlahAngkatan = JA
		self.jurusan = jur
		FakultasTeknik. __init__(self, Univ, Fak, thnajr)
	def CetakData(self):
		print("pendidikan teknik informasi dan komputer")
		print("Univ\t:",self.universitas)
		print("Fak\t:",self.fakultas)
		print("TA\t:",self.tahunAjar)
		print("JumlahAngkatan di prodi Teknik Komputer adalah",self.jumlahAngkatan)
		print(100*"=")

def main():

	a = FakultasTeknik("UNIVERSITAS NEGERI MAKASSAR", "TEKNIK", 2018)
	a.CetakData()

	del a

	a = TeknikKomputer("UNIVERSITAS NEGERI MAKASSAR", "TEKNIK", 2018, 2)
	a.CetakData()

	b = TeknikMekatronika("UNIVERSITAS NEGERI MAKASSAR","TEKNIK",2018, 2)
	b.CetakData()

	del b

	b = PTIK("UNIVERSITAS NEGERI MAKASSAR","TEKNIK", 2018, 10, "Pendidikan Teknik Elektro")
	b.CetakData()

if __name__=="__main__":
	main()


























