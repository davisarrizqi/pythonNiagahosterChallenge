AP='cls'
AO='     Input tidak valid!'
AN='descending'
AM='ascending'
AL='     Hasilnya --> %s adalah bilangan %s'
AK='     Bilangan yang akan diuji --> '
AJ='    '
AI='     Value tidak valid!\n'
m='0'
l=None
U='     +'
R='  '
Q='\n'
P='     |'
N='+'
M='-'
L='|'
K=str
J=float
G=int
F=' '
E=input
D=len
C=range
B=''
A=print
import calendar as n,math as V,random as o,os,time
class p:
	def helloWorld(I):
		E='Hello World!';A(Q);A(U,end=B)
		for G in C(D(E)*3):A(M,end=B)
		A(N);A(P,end=B)
		for H in C(D(E)*3):A(F,end=B)
		A(L);A(P,end=B)
		for G in C(D(E)):A(F,end=B)
		A(E,end=B)
		for H in C(D(E)):A(F,end=B)
		A(L);A(P,end=B)
		for H in C(D(E)*3):A(F,end=B)
		A(L);A(U,end=B)
		for G in C(D(E)*3):A(M,end=B)
		A(N)
class q:
	def duaAngka(H):
		A("\n              SIMULASI PYTHON INTERPRETER\n   +-----------------------------------------------+\n   | CODE:                                         |\n   |   aku = 6                                     |\n   |   kamu = -5                                   |\n   |   kita = aku + kamu                           |\n   +-----------------------------------------------+\n   +-----------------------------------------------+\n   |   if kita == 1: kita = 'Berati kita satu';    |\n   |   else: kita = 'Berarti kita belum bersatu';  |\n   |   print(kita)                                 |\n   +-----------------------------------------------+\n\n   +-----------------------------------------------+\n   | OUTPUT:                                       |\n   | ",end=B);D,E=6,-5;G=D+E
		if G==1:
			A('  Berarti kita satu',end=B)
			for I in C(27):A(F,end=B)
			A(L)
		else:A('  Berarti kita belum bersatu')
		A('   +-----------------------------------------------+')
class r:
	def menghitungAkarKuadrat(C):
		try:
			A('\n                  AKAR KUADRAT');B=J(E('     Masukkan bilangan yang akan anda akarkan: '))
			if B!=l:
				if B!=0:B=V.sqrt(B);A('     Hasilnya -->',B)
				else:A('     Angka tidak boleh nol!');menghitungAkarKuadrat()
			else:menghitungAkarKuadrat()
		except:A(AI);menghitungAkarKuadrat()
class s:
	def __init__(A,luas):
		if luas>25:A.luas=25
		else:A.luas=luas
	def gambarSegitiga(D):
		for E in C(D.luas):
			A(AJ,end=B)
			for G in C(D.luas-E):A(F,end=B)
			for H in C(E):A(' A',end=B)
			A(B)
	def gambarSegitigaKedua(B,tinggi,luas,alas):A('\n\n   VISUALISASI SEGITIGA\n\n             A        ]   Tinggi = %s\n            A A       |\n           A A A      |\n          A A A A     |\n         A A A A A    | \n        A A A A A A   | \n       A A A A A A A  |   \n      A A A A A A A A ]   Luas = 1/2 (Alas x Tinggi)\n   +------------------+        = %s\n         Alas = %s'%(tinggi,luas,alas))
class t:
	def __init__(A,panjang,lebar,tinggi):A.panjang=panjang;A.lebar=lebar;A.tinggi=tinggi
	def bulatkan(B,bilangan):
		A=bilangan
		if G(A)==A:A=G(A);return A
		else:return A
	def visualisasikan(B):B.panjang=B.bulatkan(B.panjang);B.lebar=B.bulatkan(B.lebar);B.tinggi=B.bulatkan(B.tinggi);A('        \n                  Panjang: %s\n              <-------------------->\n            +------------------------+ \n           /|                       /|  <>\n          / |                      / |   |\n         /  |                     /  |   | Tinggi: %s\n        +------------------------+   |   |\n        |   |____________________|___|  <>\n        |  /                     |  /\n        | /                      | / ]--- Lebar --> %s \n        |/                       |/\n        +------------------------+\n\n            Volume = Panjang x Lebar x Tinggi\n                   = %s\n\n             '%(B.panjang,B.tinggi,B.lebar,B.panjang*B.tinggi*B.lebar))
class u:
	def kuadratkan(B,bilangan,pangkat=2):
		A=1
		for D in C(pangkat):A*=bilangan
		B.hasil=A
		if G(A)==A:A=G(A)
		return A
	def akarkan(B,hasil):
		A=hasil
		if A==l:
			if B.hasil!=l:A=B.hasil
		else:A=G(A)
		A=V.sqrt(A)
		if G(A)==A:A=G(A)
		return A
W,AQ,v,X,w,x,y='A','I','S','P','D','V',F
class Y:
	def __init__(A,kkm=75):
		A.kkm=kkm;A.daftarNilainya={'Davis':98,'Rosee':92,'Haris':93,'Syafiq':95,'Nayra':90,'Budi':75,'Rahmat':67,'Putra':78,'Bahtiar':80,'Jajang':64,'Sasuke':61,'Jasuke':59};A.listNilai=[]
		for B in A.daftarNilainya:A.listNilai.append(A.daftarNilainya[B])
		A.daftarNama={m:'DAVIS ARRIZQI','1':'ROSE MAYLEE','2':'ABU HARIS','3':'SYAFIQ ARRAIS','4':'NAYRA SAFIYYA','5':'BUDI DARMAWAN','6':'RAHMAT SEJATI','7':'PUTRA TEGUH S','8':'BAHTIAR SURYA','9':'JAJANG KUJANG','10':'BAPAK SASUKEE','11':'JASUKEE NARTO'}
	def bulatkan(N,bilangan):
		E=[];L=[];A=K(bilangan);H=B
		for F in A:E.append(F)
		for I in C(D(E)):
			if E[I]=='.':M=I
		for I in C(D(E)):
			if I<M:L.append(E[0]);E.pop(0)
		E.insert(0,m);A=B
		for F in E:A+=F
		A=J(A)
		if A>0.5:A=1
		else:A=0
		for F in L:H+=F
		H=G(H)+A;return H
	def aturSpasi(A,jumlahKarakter,karakterMaksimal=21):B=A.bulatkan((karakterMaksimal-jumlahKarakter)/2);return B
	def tampilkanTabel(E):
		O='\n    |';A('\n\n                       TABEL DIBUAT OLEH DAVIS APP\n');H=0;A('    +',end=B)
		for G in C(3):
			for G in C(20):A(M,end=B)
			A(N,end=B)
		A(O,end=B)
		for G in C(3):
			for G in C(10):A(R,end=B)
			A(L,end=B)
		A('\n    |   NAMA PANGGILAN   ',end=B);A('|     NILAI AKHIR    ',end=B);A('|    STATUS SISWA    |',end=B);A(O,end=B)
		for G in C(3):
			for G in C(10):A(R,end=B)
			A(L,end=B)
		A('\n    +',end=B)
		for G in C(3):
			for G in C(20):A(M,end=B)
			A(N,end=B)
		for H in C(D(E.daftarNama)):
			A(O,end=B)
			for G in C(3):
				for G in C(10):A(R,end=B)
				A(L,end=B)
			P=E.aturSpasi(D(E.daftarNama[K(H)]))-1;A(O,end=B);A(F*P,end=B);A(E.daftarNama[K(H)],end=B);A(F*E.aturSpasi(D(E.daftarNama[K(H)])),end=B);A(L,end=B);A(F*E.aturSpasi(D(K(E.listNilai[H]))),end=B);A(E.listNilai[H],end=B);A(F*E.aturSpasi(D(K(E.listNilai[H]))),end=B);I=B
			if E.listNilai[H]>E.kkm:I='LULUS'
			else:I='TIDAK LULUS'
			A(L,end=B);A(F*E.aturSpasi(D(I)),end=B);A(I,end=B);A(F*(E.aturSpasi(D(I))-1),end=B);A(L,end=B);H+=1;A(O,end=B)
			for G in C(3):
				for G in C(10):A(R,end=B)
				A(L,end=B)
			J=B
			if H==D(E.daftarNama)-1:J=N
			else:J=L
			A('\n    ',J,end=B,sep=B)
			for G in C(3):
				for G in C(20):A(M,end=B)
				A(J,end=B)
	def daftarLulus(A):
		A.yangLulus=[]
		for B in A.daftarNilainya:
			C=A.daftarNilainya[B]
			if C>=A.kkm:A.yangLulus.append(B)
			else:0
		return A.yangLulus
	def daftarTakLulus(A):
		A.yangTakLulus=[]
		for B in A.daftarNilainya:
			C=A.daftarNilainya[B]
			if C<A.kkm:A.yangTakLulus.append(B)
			else:0
		return A.yangTakLulus
	def namaPanggilan(I,nama):
		G=[];A=B
		for E in C(D(nama)):
			A=nama[E]
			if A!=F:0
			else:break
			if E!=0 and A.isupper():A=A.lower()
			elif E==0:A=A.upper()
			G.append(A)
		A=B
		for H in G:A+=H
		return A
	def jadikanKapital(F,kata):
		C=[];D=B
		for A in kata:A=A.upper();C.append(A)
		for E in C:D+=E
		return D
	def duaKata(H,nama):
		C=[];E=B;D=0
		for A in nama:
			if A!=F:C.append(A)
			elif A==F and D==0:D=1;C.append(A)
			elif A==F and D==1:break
		for G in C:E+=K(G)
		return E
	def tambahkanSiswa(H):
		M='namaKepanjangan'
		try:
			C=E('     Masukkan Nama: ')
			if D(C)>17:C=H.duaKata(C)
			if D(C)>17:I=M;raise
			else:
				I=B
				if D(C)%2==0:C=F+C
			J=G(E('     Masukkan Nilai: '))
			if J>99:raise
			else:0
			L=K(D(H.daftarNama));C=H.jadikanKapital(C);H.listNilai.append(J);H.daftarNama.setdefault(L,C);H.tampilkanTabel()
		except:
			if I==M:A('     Nama terlalu panjang!, maksimal 2 kata 17 Karakter!\n');tambahkanSiswa()
			else:A('     Terjadi error, silahkan mengulangi');tambahkanSiswa()
	def mulaiEksekusi(B,kodenya):
		C=kodenya
		if C==0:B.tampilkanTabel()
		elif C==1:B.tambahkanSiswa()
		elif C==2:A('     Siswa yang lulus adalah: ',B.daftarLulus())
		elif C==3:A('     Siswa yang tidak lulus adalah: ',B.daftarTakLulus())
		elif C==4:D='     Kami menggunakan KKM '+K(B.kkm)+' dalam pendidikan kami';A(D)
		else:0
class z:
	def __init__(A):A.owner=w+W+x+v+y+W+X+X;A.topScorer=0;A.database=Y();A.panjang=A.database.aturSpasi(D(A.owner*2));A.status='safe'
	def watermark(E):
		try:
			A(U,end=B)
			for G in C(D(E.owner)*3):A(M,end=B)
			A(N);A(P,end=B)
			for G in C(D(E.owner)*3):A(F,end=B)
			A(L);A(P,end=B)
			for G in C(D(E.owner)):A(F,end=B)
			A(E.owner,end=B)
			for G in C(D(E.owner)):A(F,end=B)
			A(L);A(P,end=B)
			for G in C(D(E.owner)*3):A(F,end=B)
			A(L);A(U,end=B)
			for G in C(D(E.owner)*3):A(M,end=B)
			A(N)
		except:A('Input invalid, silahkan mengulangi!');watermark()
	def halamanUtama(C):
		C.watermark();A(B);A('        ---> MAIN MENU <---','   1.  Tampilkan Hello World','   2.  Menjumlahkan Dua Angka','   3.  Menghitung Akar Kuadrat','   4.  Menghitung Luas Segitiga','   5.  Menghitung Volume Kubus','   6.  Menyelesaikan Persamaan Kuadrat','   7.  Menukar Dua Variabel','   8.  Menghasilkan Angka Acak','   9.  Mengubah Kilometer Menjadi Mil','   10. Mengubah Celcius Menjadi Fahrenheit','   11. Menentukan Bilangan Positif, Negatif, atau Nol','   12. Menentukan Bilangan Ganjil atau Genap','   13. Menentukan Tahun Kabisat','   14. Menampilkan Kalender Masehi','   15. Mengurutkan Kata Sesuai Abjad','   16. Menampilkan Tabel Perkalian','   17. Menentukan Nilai dan Kelulusan',sep=Q,end=Q);C.listKode=['1.TampilkanHelloWorld','2.MenjumlahkanDuaAngka','3.MenghitungAkarKuadrat','4.MenghitungLuasSegitiga','5.MenghitungVolumeKubus','6.MenyelesaikanPersamaanKuadrat','7.MenukarDuaVariabel','8.MenghasilkanAngkaAcak','9.MengubahKilometerMenjadiMil','10.MengubahCelciusMenjadiFahrenheit','11.MenentukanBilanganPositifNegatifatauNol','12.MenentukanBilanganGanjilatauGenap','13.MenentukanTahunKabisat','14.MenampilkanKalenderMasehi','15.MengurutkanKataSesuaiAbjad','16.MenampilkanTabelPerkalian','17.MenentukanNilaidanKelulusan'];C.kode=E('      --> Kode untuk ditampilkan: ')
		if C.kode=='exit':A(os.abort())
		else:0
		try:C.kode=G(C.kode);C.topScorer=C.kode
		except:C.alternateSearch()
	def defaultSearch(N):
		H,Q=N.listKode,N.kode;F,I=B,[];J,K,G,E,L,W=[],0,[],[],0,B
		for M in C(D(H)):
			for R in C(D(H[M])):G.append(H[M][R])
			for S in Q:E.append(S)
			for O in C(D(E)):
				for T in C(D(G)):
					if E[O]==G[T]:I.append(E[O]);L+=1
			for U in F:I.append(U)
			F=B
			for V in I:F+=V
			J.append(L);A(J)
			if M==D(H)-1:
				for P in J:
					if K<P:K=P
				A(K);A(F);A(G);A(E);A('Rose Maylee')
			L=0;G.clear();E.clear();F=B;I.clear()
	def alternateSearch(I):
		G,J=I.listKode,I.kode;H,K,N=[],[],0;O,P,M,Q=[],[],0,B
		for A in J:P.append(A)
		for A in C(D(J)):K.append(D(J)-A)
		K.append(0);K.sort()
		for A in C(D(G)):
			for E in C(D(G[A])):
				if E==D(G[A])-1:break
				else:
					for L in C(D(K)):
						if L==D(K)-2:break
						elif L==C(D(G[A][E])):break
						if J[L]==G[A][E]and J[L+1]==G[A][E+1]:M+=1
			O.append(A);H.append(M);M=0
		F=0
		for A in H:
			if F<A:F=A
		for E in C(D(H)):
			if F==H[E]:F=E;break
		F+=1
		for R in C(D(H)):
			if F in H:N+=1
		I.topScorer=F;I.status=Q;I.checker=N
helloWorld=p()
A0=q()
akarkan=r()
def Z():
	try:
		C=J(E('\n    Masukkan alas segitiga: '));D=J(E('    Masukkan tinggi segitiga: '));B=1/2*(C*D)
		if G(B)==B:B=G(B)
		else:0
		F=s(G(B));F.gambarSegitigaKedua(D,B,C);A('\n    Jadi, luas dari segitiga tersebut adalah:',B)
	except:A('    Value tidak valid!\n');Z()
def a():
	try:A('\n                                                VISUALISASI KUBUS');B=J(E('\n     Masukkan panjang kubus: '));C=J(E('     Masukkan lebar kubus: '));D=J(E('     Masukkan tinggi kubus: '));F=t(B,C,D);F.visualisasikan()
	except:A(AI);a()
def b():
	G='     Hasilnya adalah: ';C=['Kuadratkan','Akarkan'];A('\n           Kuadratkan || Akarkan');B=0;F=u()
	try:
		D=E('     Yang akan anda pilih adalah: ')
		if D in C and D==C[0]:B=J(E('     Angka yang akan dikuadratkan: '));B=F.kuadratkan(B);A(G,B)
		elif D in C and D==C[1]:B=J(E('     Angka yang akan diakarkan: '));B=F.akarkan(B);A(G,B)
		else:raise
	except:A('     Jawaban tidak valid, kode harus sama persis dengan yang ditampilkan!\n');b()
def c(a,b):a,b=b,a;return a,b
def H(atj):
	A=atj;D=A;A=K(A);list=[]
	for C in A:list.append(C)
	if list[-1]==m and list[-2]=='.':
		list.pop(-1);list.pop(-1);A=B
		for C in list:A+=C
		A=G(A);return A
	else:return D
def AR():B=18;C=8;B,C=c(B,C);A(B,C)
def A1():F='dan';A('\n\n              PENUKARAN BILANGAN\n');C=J(E('    Angka pertama yang akan dimasukkan: '));D=J(E('    Angka kedua yang akan dimasukkan: '));A(B);C=H(C);D=H(D);A('    Sebelum ditukar bilangan 1 dan 2:',C,F,D);C,D=c(C,D);C=H(C);D=H(D);A('    Sesudah ditukar bilangan 1 dan 2:',C,F,D);A('\n    Metode yang digunakan --> [A, B = B, A]')
def A2(a,b):A=o.randint(a,b);return A
def d(hasil=0):
	G='   +-------------------------+';F=hasil;A(B)
	try:
		A('\n       Hasilkan Angka Acak');A(G);C=J(E('    Bilangan dimulai dari --> '));D=J(E('    dan batasnya hingga --> '));A(G);H(C);H(D)
		if C>D:A('    Note: Bilangan awal < Bilangan akhir (Batasnya)');raise
		else:F=A2(C,D)
		A('       Hasil Angka Acak -->',F);A(B)
	except:A('    Bilangan tidak valid!');d()
def A3(kilometer):A=kilometer;B=1.609;A*=B;return A
def A4(mil):A=1.609;mil/=1.609;return mil
def e():
	S='Konversi Antara Km dan Mil';R='       +';P='       --> Maka %s %s = %s';I=['km','mil'];A('\n        Konversi Antara Km dan Mil');A(R,end=B)
	for Q in C(D(S)):A(M,end=B)
	A(N);G=E('       Satuan Awal --> ');L=E('       Satuan Akhir --> ');A(R,end=B)
	for Q in C(D(S)):A(M,end=B)
	A(N)
	if G and L in I:
		F=J(E('       Angka yang akan dikonversikan: '));O=K(F)
		if G==I[0]and L==I[1]:F=A3(F);H(F);F=K(F)+L;A(P%(O,G,F))
		elif G==I[1]and L==I[0]:F=A4(F);H(F);F=K(F)+L;A(P%(O,G,F))
		else:H(F);F=K(F)+G;A(P%(O,G,F))
	else:A('     Pilihlah antara "mil" ke "km" atau "km" ke "mil"!\n');e()
def A5(c):A=c*9/5+32;H(A);return A
def A6(f):A=(f-32)*5/9;H(A);return A
def f():
	L='    +--------------------------------+';G=['C','F'];A('\n      Konversi Celcius ke Fahrenheit');A(L);A('      Satuan yang tersedia --> C dan F')
	try:
		C=E('      Satuan awalnya adalah: ');D=E('      Satuan akhirnya adalah: ');C=C.upper();D=D.upper()
		if C not in G or D not in G:raise
		elif C and D in G:
			B=J(E('      Angka yang akan diubah: '));I=H(B);A(L)
			if C==G[0]and D==G[1]:B=A5(B);H(B);B=K(B)+F+D
			elif C==G[1]and D==G[0]:B=A6(B);H(B);B=K(B)+F+D
			else:B=B;H(B);B=K(B)+F+C
			A('      Hasilnya --> %s %s = %s'%(I,C,B))
	except:A('      Pilihlah antara C dan F !');f()
O=['Positif','Negatif','Nol','Bukan Positif, Negatif, atau Nol']
def A7(bilangan):
	B=bilangan
	if B>0:A=O[0]
	elif B<0:A=O[1]
	elif B==0:A=O[2]
	else:A=O[3]
	return A
def g():
	A(B)
	try:
		A('             UJI BILANGAN POSITIF ATAU NEGATIF');C=J(E(AK));D=H(C);C=A7(C)
		if C in O:A(AL%(D,C))
		else:raise
	except:A('     Bilangan tidak terdefinisi!');g()
def A8(bilangan):
	A=bilangan
	if G(A)and A%2==0:A='genap'
	elif J(A)and A%2!=0:A='ganjil dan bukan genap'
	else:A='yang bukan ganjil dan bukan genap'
	return A
def A9():A('\n          PERIKSA BILANGAN GANJIL ATAU GENAP');B=J(E(AK));B=H(B);C=B;B=A8(B);A(AL%(C,B))
def AA(tahun):
	A=tahun
	if A%4==0:A='adalah tahun kabisat'
	elif A%4!=0:A='bukan tahun kabisat'
	else:A='merupakan tahun yang tak terdefinisi'
	return A
def h():
	A(B)
	try:A('             UJI KABISAT PADA TAHUN MASEHI');C=G(E('     Anda akan menguji tahun masehi --> '));D=C;C=AA(C);A('     Hasilnya --> %s %s'%(D,C))
	except:A('     Tahun tak terdefinisi!');h()
def AB(tahun):A(n.calendar(tahun))
def i():
	A(B)
	try:C=G(E('     Anda akan menampilkan kalender untuk tahun: '));A(B);AB(C)
	except:A('     Tahun tidak valid!');i()
def AC(word):
	A=word;A=sorted(A);C=B
	for D in A:C+=D
	return C
def AD(wordlist,sortingType=AM):
	F=sortingType;A=wordlist
	for B in A:
		try:B=G(B)
		except:pass
	if F==AN or F=='Descending':
		for B in C(D(A)):
			for E in C(D(A)):
				if A[B]>A[E]:A[B],A[E]=A[E],A[B]
				else:0
	elif F==AM or F=='Ascending':
		for B in C(D(A)):
			for E in C(D(A)):
				if A[B]<A[E]:A[B],A[E]=A[E],A[B]
				else:0
	return A
def AE():
	try:A('\n                    PENGURUTAN HURUF');B=E('     Masukkan konten apa yang akan diurutkan --> ');A('     Sebelum diurutkan -->',B);B=AC(B);A('     Sesudah diurutkan -->',B)
	except:A(AO);mulaiPengurutan()
def AF():
	A(B)
	try:
		list=[];D=G(E('Jumlah anggota list yang akan dimasukkan: '))
		for F in C(D):A('Masukkan konten ke',F+1,end=' --> ');H=G(E(B));list.append(H)
		list=AD(list,AN);A(list)
	except:A('Input tidak valid!');AF()
def AG(horizontal,vertikal):
	A=[];B=['X']
	for D in C(horizontal):A.append(D+1)
	for E in C(vertikal):B.append(E+1)
	return A,B
def S(bilangan):A=bilangan;A=K(A);B=5-D(A)-1;return B*F
def AH(horizontal=10,vertical=10):
	A('\n\n      TABEL PERKALIAN DAVIS APP\n');I,F=AG(horizontal,vertical)
	for E in C(D(F)):
		A('     ',F[E],end=S(F[E]))
		for G in I:
			if E==0:A(G,end=S(G))
			else:H=E*G;A(H,end=S(H))
		A(B)
def j():
	A(B)
	try:C=G(E('     Panjang Horizontal: '));D=G(E('     Panjang Vertical: '));AH(C,D)
	except:A(AO);j()
def k():
	J=[B,F,R,'   ',AJ]
	try:
		K=Y();H=['1Tampilkan Tabel','2Tambahkan Siswa','3Daftar Siswa Lulus','4Daftar Siswa Tak Lulus','5KKM Yang Digunakan'];A('\n\n                       DATABASE BY DAVIS APP');A('\n      Fungsi Tersedia: ');A('      1. Tampilkan Tabel','      2. Tambahkan Siswa','      3. Daftar Siswa Lulus','      4. Daftar Siswa Tak Lulus','      5. KKM Yang Digunakan',sep=Q,end=Q);G=E('      Nomor yang anda pilih: ');A(B)
		for I in C(D(H)):
			if G in J or G==0:raise
			elif G in H[I]:K.mulaiEksekusi(I)
	except:A('      Input value tidak valid, silahkan mengulangi!\n');k()
def I():E('\n\n     Tekan Enter Untuk Kembali ke Beranda\n');os.system(AP);T()
def T():
	try:
		C=z();C.halamanUtama();B=C.topScorer
		if B==1:helloWorld.helloWorld();I()
		elif B==2:A0.duaAngka();I()
		elif B==3:akarkan.menghitungAkarKuadrat();I()
		elif B==4:Z();I()
		elif B==5:a();I()
		elif B==6:b();I()
		elif B==7:A1();I()
		elif B==8:d();I()
		elif B==9:e();I()
		elif B==10:f();I()
		elif B==11:g();I()
		elif B==12:A9();I()
		elif B==13:h();I()
		elif B==14:i();I()
		elif B==15:AE();I()
		elif B==16:j();I()
		elif B==17:k();I()
		else:raise
	except:A('     Input Gagal, Mengulang Kembali\n');time.sleep(2);os.system(AP);T()
T()
