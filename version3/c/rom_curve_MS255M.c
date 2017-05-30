#include "arch.h"
#include "ecp_MS255M.h"

/* MS255 NUMS Curve - Montgomery */

/* Pseudo-Mersenne NUMS curves http://eprint.iacr.org/2014/130 */


#if CHUNK==32
const int CURVE_A_MS255M=-240222;
const BIG_256 CURVE_Order_MS255M= {0x436EB75,0x24E8F68,0x9A0CBAB,0x34F0BDB,0x1FFFFDCF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFF};
const BIG_256 CURVE_Gx_MS255M= {0x4};

#endif

#if CHUNK==64
const int CURVE_A_MS255M=-240222;
const BIG_256 CURVE_Order_MS255M= {0x49D1ED0436EB75,0xA785EDA6832EAC,0xFFFFFFFFFFDCF1,0xFFFFFFFFFFFFFF,0x1FFFFFFF};
const BIG_256 CURVE_Gx_MS255M= {0x4};

#endif