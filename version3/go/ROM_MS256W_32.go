/*
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
*/

/* Fixed Data in ROM - Field and Curve parameters */

package MS256W

var Modulus= [...]Chunk {0x1FFFFF43,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0xFFFFFF}
const MConst Chunk=0xBD

const CURVE_A int= -3
var CURVE_B = [...]Chunk {0x25581,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0}
var CURVE_Order = [...]Chunk {0x751A825,0x559014A,0x9971808,0x1904EBD4,0x1FFFFE43,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0xFFFFFF}
var CURVE_Gx = [...]Chunk {0x1,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0}
var CURVE_Gy = [...]Chunk {0x2B56C77,0x1FA31836,0x253B042,0x185F26EB,0xDD6BD02,0x4B66777,0x1B5FF20B,0xA783C8C,0x696F18}
