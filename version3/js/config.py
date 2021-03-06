import os
import sys

deltext=""
slashtext=""
copytext=""
if sys.platform.startswith("linux")  :
	copytext="cp "
	deltext="rm "
	slashtext="/"
if sys.platform.startswith("win") :
	copytext="copy "
	deltext="del "
	slashtext="\\"

def replace(namefile,oldtext,newtext):
	f = open(namefile,'r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace(oldtext,newtext)

	f = open(namefile,'w')
	f.write(newdata)
	f.close()

def addit(fname):
	if fname not in open("include.html").read():
		with open("include.html","a") as incfile:
			incfile.write("<script type=\"text/javascript\" src=\""+fname+"\"></script>\n")

def rsaset(tb,tff,nb,base,ml) :

	fname="BIG_"+tb+".js"
	os.system(copytext+" BIG_XXX.js "+fname)

	replace(fname,"XXX",tb)
	replace(fname,"@NB@",nb)
	replace(fname,"@BASE@",base)
	addit(fname)

	fname="DBIG_"+tb+".js"
	os.system(copytext+" DBIG_XXX.js "+fname)

	replace(fname,"XXX",tb)
	addit(fname)


	fname="FF_"+tff+".js"
	os.system(copytext+" FF_WWW.js "+fname)

	replace(fname,"WWW",tff)
	replace(fname,"XXX",tb)
	replace(fname,"@ML@",ml)
	addit(fname)

	fname="RSA_"+tff+".js"
	os.system(copytext+" RSA_WWW.js "+fname)

	replace(fname,"WWW",tff)
	replace(fname,"XXX",tb)
	addit(fname)


def curveset(tb,tf,tc,nb,base,nbt,m8,mt,ct,pf) :

	fname="BIG_"+tb+".js"
	os.system(copytext+" BIG_XXX.js "+fname)

	replace(fname,"XXX",tb)
	replace(fname,"@NB@",nb)
	replace(fname,"@BASE@",base)
	addit(fname)

	fname="DBIG_"+tb+".js"
	os.system(copytext+" DBIG_XXX.js "+fname)

	replace(fname,"XXX",tb)
	addit(fname)

	fname="FP_"+tf+".js"
	os.system(copytext+" FP_YYY.js "+fname)

	replace(fname,"XXX",tb)
	replace(fname,"YYY",tf)
	replace(fname,"@NBT@",nbt)
	replace(fname,"@M8@",m8)
	replace(fname,"@MT@",mt)
	addit(fname)

	fname="ECP_"+tc+".js"
	os.system(copytext+" ECP_ZZZ.js "+fname)

	replace(fname,"XXX",tb)
	replace(fname,"YYY",tf)
	replace(fname,"ZZZ",tc)
	replace(fname,"@CT@",ct)
	replace(fname,"@PF@",pf)
	addit(fname)

	fname="ECDH_"+tc+".js"
	os.system(copytext+" ECDH_ZZZ.js "+fname)

	replace(fname,"ZZZ",tc)
	replace(fname,"YYY",tf)
	replace(fname,"XXX",tb)
	addit(fname)

	fname="ROM_FIELD_"+tf+".js"
	addit(fname)
	fname="ROM_CURVE_"+tc+".js"
	addit(fname)

	if pf != "NOT" :
		fname="FP2_"+tf+".js"
		os.system(copytext+" FP2_YYY.js "+fname)
		replace(fname,"YYY",tf)
		replace(fname,"XXX",tb)
		addit(fname)

		fname="FP4_"+tf+".js"
		os.system(copytext+" FP4_YYY.js "+fname)
		replace(fname,"YYY",tf)
		replace(fname,"XXX",tb)
		addit(fname)

		fname="FP12_"+tf+".js"
		os.system(copytext+" FP12_YYY.js "+fname)
		replace(fname,"YYY",tf)
		replace(fname,"XXX",tb)
		addit(fname)

		fname="ECP2_"+tc+".js"
		os.system(copytext+" ECP2_ZZZ.js "+fname)
		replace(fname,"YYY",tf)
		replace(fname,"XXX",tb)
		replace(fname,"ZZZ",tc)
		addit(fname)

		fname="PAIR_"+tc+".js"
		os.system(copytext+" PAIR_ZZZ.js "+fname)
		replace(fname,"YYY",tf)
		replace(fname,"XXX",tb)
		replace(fname,"ZZZ",tc)
		addit(fname)

		fname="MPIN_"+tc+".js"
		os.system(copytext+" MPIN_ZZZ.js "+fname)
		replace(fname,"YYY",tf)
		replace(fname,"XXX",tb)
		replace(fname,"ZZZ",tc)
		addit(fname)

print("Elliptic Curves")
print("1. ED25519")
print("2. C25519")
print("3. NIST256")
print("4. BRAINPOOL")
print("5. ANSSI")
print("6. HIFIVE")
print("7. GOLDILOCKS")
print("8. NIST384")
print("9. C41417")
print("10. NIST521\n")
print("11. MF254 WEIERSTRASS")
print("12. MF254 EDWARDS")
print("13. MF254 MONTGOMERY")
print("14. MF256 WEIERSTRASS")
print("15. MF256 EDWARDS")
print("16. MF256 MONTGOMERY")
print("17. MS255 WEIERSTRASS")
print("18. MS255 EDWARDS")
print("19. MS255 MONTGOMERY")
print("20. MS256 WEIERSTRASS")
print("21. MS256 EDWARDS")
print("22. MS256 MONTGOMERY")


print("Pairing-Friendly Elliptic Curves")
print("23. BN254")
print("24. BN254CX")
print("25. BLS383\n")

print("RSA")
print("26. RSA2048")
print("27. RSA3072")
print("28. RSA4096")

selection=[]
ptr=0
max=29

curve_selected=False
pfcurve_selected=False
rsa_selected=False

while ptr<max:
	x=int(input("Choose a Scheme to support - 0 to finish: "))
	if x == 0:
		break
#	print("Choice= ",x)
	already=False
	for i in range(0,ptr):
		if x==selection[i]:
			already=True
			break
	if already:
		continue
	
	selection.append(x)
	ptr=ptr+1

# curveset(big,field,curve,big_length_bytes,16_bit_bits_in_base,32_bit_bits_in_base,64_bit_bits_in_base,modulus_bits,modulus_mod_8,modulus_type,curve_type,pairing_friendly)
# for each curve give names for big, field and curve. In the latter two cases the names may be the same.
# Typically "big" is the size in bits, always a multiple of 8, "field" describes the modulus, and "curve" is the common name for the elliptic curve   
# big_length_bytes is "big" divided by 8
# Next give the number base used for 16/32/64 bit architectures, as n where the base is 2^n (note that these must be fixed for the same "big" name, if is ever re-used for another curve)
# modulus_bits is the bit length of the modulus, typically the same or slightly smaller than "big"
# modulus_mod_8 is the remainder when the modulus is divided by 8
# modulus_type is NOT_SPECIAL, or PSEUDO_MERSENNE, or MONTGOMERY_Friendly, or GENERALISED_MERSENNE (supported for GOLDILOCKS only)
# curve_type is WEIERSTRASS, EDWARDS or MONTGOMERY
# pairing_friendly is BN, BLS or NOT (if not pairing friendly

	if x==1:
		curveset("256","25519","ED25519","32","24","255","5","PSEUDO_MERSENNE","EDWARDS","NOT")
		curve_selected=True
	if x==2:
		curveset("256","25519","C25519","32","24","255","5","PSEUDO_MERSENNE","MONTGOMERY","NOT")
		curve_selected=True
	if x==3:
		curveset("256","NIST256","NIST256","32","24","256","7","NOT_SPECIAL","WEIERSTRASS","NOT")
		curve_selected=True
	if x==4:
		curveset("256","BRAINPOOL","BRAINPOOL","32","24","256","7","NOT_SPECIAL","WEIERSTRASS","NOT")
		curve_selected=True
	if x==5:
		curveset("256","ANSSI","ANSSI","32","24","256","7","NOT_SPECIAL","WEIERSTRASS","NOT")
		curve_selected=True

	if x==6:
		curveset("336","HIFIVE","HIFIVE","42","23","336","5","PSEUDO_MERSENNE","EDWARDS","NOT")
		curve_selected=True
	if x==7:
		curveset("448","GOLDILOCKS","GOLDILOCKS","56","23","448","7","GENERALISED_MERSENNE","EDWARDS","NOT")
		curve_selected=True
	if x==8:
		curveset("384","NIST384","NIST384","48","","28","56","384","7","NOT_SPECIAL","WEIERSTRASS","NOT")
		curve_selected=True
	if x==9:
		curveset("416","C41417","C41417","52","23","414","7","PSEUDO_MERSENNE","EDWARDS","NOT")
		curve_selected=True
	if x==10:
		curveset("528","NIST521","NIST521","66","23","521","7","PSEUDO_MERSENNE","WEIERSTRASS","NOT")
		curve_selected=True

	if x==11:
		curveset("256","254MF","MF254W","32","24","254","7","MONTGOMERY_FRIENDLY","WEIERSTRASS","NOT")
		curve_selected=True
	if x==12:
		curveset("256","254MF","MF254E","32","24","254","7","MONTGOMERY_FRIENDLY","EDWARDS","NOT")
		curve_selected=True
	if x==13:
		curveset("256","254MF","MF254M","32","24","254","7","MONTGOMERY_FRIENDLY","MONTGOMERY","NOT")
		curve_selected=True
	if x==14:
		curveset("256","256MF","MF256W","32","24","256","7","MONTGOMERY_FRIENDLY","WEIERSTRASS","NOT")
		curve_selected=True
	if x==15:
		curveset("256","256MF","MF256E","32","24","256","7","MONTGOMERY_FRIENDLY","EDWARDS","NOT")
		curve_selected=True
	if x==16:
		curveset("256","256MF","MF256M","32","24","256","7","MONTGOMERY_FRIENDLY","MONTGOMERY","NOT")
		curve_selected=True
	if x==17:
		curveset("256","255MS","MS255W","32","24","255","3","PSEUDO_MERSENNE","WEIERSTRASS","NOT")
		curve_selected=True
	if x==18:
		curveset("256","255MS","MS255E","32","24","255","3","PSEUDO_MERSENNE","EDWARDS","NOT")
		curve_selected=True
	if x==19:
		curveset("256","255MS","MS255M","32","24","255","3","PSEUDO_MERSENNE","MONTGOMERY","NOT")
		curve_selected=True
	if x==20:
		curveset("256","256MS","MS256W","32","24","256","3","PSEUDO_MERSENNE","WEIERSTRASS","NOT")
		curve_selected=True
	if x==21:
		curveset("256","256MS","MS256E","32","24","256","3","PSEUDO_MERSENNE","EDWARDS","NOT")
		curve_selected=True
	if x==22:
		curveset("256","256MS","MS256M","32","24","256","3","PSEUDO_MERSENNE","MONTGOMERY","NOT")
		curve_selected=True

	if x==23:
		curveset("256","BN254","BN254","32","24","254","3","NOT_SPECIAL","WEIERSTRASS","BN")
		pfcurve_selected=True
	if x==24:
		curveset("256","BN254CX","BN254CX","32","24","254","3","NOT_SPECIAL","WEIERSTRASS","BN")
		pfcurve_selected=True
	if x==25:
		curveset("384","BLS383","BLS383","48","23","383","3","NOT_SPECIAL","WEIERSTRASS","BLS")
		pfcurve_selected=True

# rsaset(big,ring,big_length_bytes,bits_in_base,multiplier)
# for each choice give distinct names for "big" and "ring".
# Typically "big" is the length in bits of the underlying big number type
# "ring" is the RSA modulus size = "big" times 2^m
# big_length_bytes is "big" divided by 8
# Next give the number base as n where the base is 2^n (run check.cpp)
# multiplier is 2^m (see above)

# There are choices here, different ways of getting the same result, but some faster than others
	if x==26:
		#256 is slower but may allow reuse of 256-bit BIGs used for elliptic curve
		#512 is faster.. but best is 1024
		rsaset("1024","2048","128","22","2")
		#rsaset("512","2048","64","23","4")
		#rsaset("256","2048","32","24","8")
		rsa_selected=True
	if x==27:
		rsaset("384","3072","48","23","8")
		rsa_selected=True
	if x==28:
		#rsaset("256","4096","32","24","16")
		rsaset("512","4096","64","23","8")
		rsa_selected=True


os.system(deltext+" BIG_XXX.js")
os.system(deltext+" DBIG_XXX.js")
os.system(deltext+" FP_YYY.js")
os.system(deltext+" ECP_ZZZ.js")
os.system(deltext+" ECDH_ZZZ.js")
os.system(deltext+" FF_WWW.js")
os.system(deltext+" RSA_WWW.js")
os.system(deltext+" FP2_YYY.js")
os.system(deltext+" FP4_YYY.js")
os.system(deltext+" FP12_YYY.js")
os.system(deltext+" ECP2_ZZZ.js")
os.system(deltext+" PAIR_ZZZ.js")
os.system(deltext+" MPIN_ZZZ.js")

# create library

