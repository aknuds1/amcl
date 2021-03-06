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

package MS255E

var Modulus= [...]Chunk {0x1FFFFD03,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x7FFFFF}
const MConst Chunk=0x2FD

const CURVE_A int= -1
var CURVE_B = [...]Chunk {0xEA97,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0}
var CURVE_Order=[...]Chunk {0x436EB75,0x24E8F68,0x9A0CBAB,0x34F0BDB,0x1FFFFDCF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFF}
var CURVE_Gx =[...]Chunk {0x4,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0}
var CURVE_Gy =[...]Chunk {0x108736A0,0x11512ADE,0x1116916E,0x29715DA,0x47E5529,0x66EC706,0x1517B095,0xA694F76,0x26CB78}
