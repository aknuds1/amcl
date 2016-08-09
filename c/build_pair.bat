
gcc -std=c99 -c -O3 big.c
gcc -std=c99 -c -O3 fp.c
gcc -std=c99 -c -O3 ecp.c
gcc -std=c99 -c -O3 hash.c
gcc -std=c99 -c -O3 rand.c
gcc -std=c99 -c -O3 aes.c
gcc -std=c99 -c -O3 gcm.c
gcc -std=c99 -c -O3 oct.c
gcc -std=c99 -c -O3 rom.c

gcc -std=c99 -c -O3 fp2.c
gcc -std=c99 -c -O3 ecp2.c
gcc -std=c99 -c -O3 fp4.c
gcc -std=c99 -c -O3 fp12.c
gcc -std=c99 -c -O3 pair.c

del amcl.a
ar rc amcl.a big.o fp.o ecp.o hash.o
ar r amcl.a rand.o aes.o gcm.o oct.o rom.o

ar r amcl.a pair.o fp2.o ecp2.o fp4.o fp12.o

gcc -std=c99 -O3 testmpin.c mpin.c amcl.a -o testmpin.exe

del *.o
