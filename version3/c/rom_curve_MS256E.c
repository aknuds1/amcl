#include "arch.h"
#include "ecp_MS256E.h"

/* MS256 NUMS Curve - Edwards */

/* Pseudo-Mersenne NUMS curves http://eprint.iacr.org/2014/130 */

#if CHUNK==16
const int CURVE_A_MS256E=-1;
const BIG_256 CURVE_Order_MS256E= {0x14AD,0x915,0x1BC4,0x109C,0xE5B,0x1E32,0x29A,0xB5A,0xAA5,0x1DF3,0x1FFF,0x1FFF,0x1FFF,0x1FFF,0x1FFF,0x1FFF,0x1FFF,0x1FFF,0x1FFF,0x7F};
const BIG_256 CURVE_B_MS256E= {0x1BEE,0x1};
const BIG_256 CURVE_Gx_MS256E= {0xd};
const BIG_256 CURVE_Gy_MS256E= {0xDBA,0x18E5,0xD4C,0x1EDF,0x1707,0x181F,0x934,0xC70,0xA6D,0x1DF1,0x11AF,0x1F40,0xB39,0x998,0xE8F,0xEDB,0xA12,0xF1,0x2AD,0xFA};

#endif

#if CHUNK==32
const int CURVE_A_MS256E=-1;
const BIG_256 CURVE_Order_MS256E= {0x1122B4AD,0xDC27378,0x9AF1939,0x154AB5A1,0x1FFFFBE6,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x3FFFFF};
const BIG_256 CURVE_B_MS256E= {0x3BEE};
const BIG_256 CURVE_Gx_MS256E= {0xd};
const BIG_256 CURVE_Gy_MS256E= {0x131CADBA,0x3FB7DA9,0x134C0FDC,0x14DAC704,0x46BFBE2,0x1859CFD0,0x1B6E8F4C,0x3C5424E,0x7D0AB4};


#endif

#if CHUNK==64
const int CURVE_A_MS256E=-1;
const BIG_256 CURVE_Order_MS256E= {0xB84E6F1122B4AD,0xA55AD0A6BC64E5,0xFFFFFFFFFFBE6A,0xFFFFFFFFFFFFFF,0x3FFFFFFF};
const BIG_256 CURVE_B_MS256E= {0x3BEE};
const BIG_256 CURVE_Gx_MS256E= {0xd};
const BIG_256 CURVE_Gy_MS256E= {0x7F6FB5331CADBA,0x6D63824D303F70,0xB39FA046BFBE2A,0x2A1276DBA3D330,0x7D0AB41E};
#endif